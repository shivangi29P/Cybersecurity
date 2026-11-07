import os
import re
import csv
import time
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ABUSEIPDB_API_KEY")
TARGET_URL = "https://abuseipdb.com"
LOG_FILE = "enterprise_auth.log"
OUTPUT_FILE = "threat_report.csv"
IP_REGEX = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

def parse_failed_logins(path):
    targets = set()
    try:
        with open(path, "r", encoding="utf-8") as src:
            for line in src:
                if "Failed password" in line:
                    match = re.search(IP_REGEX, line)
                    if match:
                        targets.add(match.group())
    except FileNotFoundError:
        print(f"[-] Execution halted: Source log file '{path}' not found.")
    return targets

def query_threat_reputation(ip, token):
    params = {"ipAddress": ip, "maxAgeInDays": "90"}
    headers = {"Accept": "application/json", "Key": token}
    
    try:
        response = requests.get(TARGET_URL, headers=headers, params=params)
        if response.status_code == 200:
            payload = response.json().get("data", {})
            return {
                "ip": ip,
                "country": payload.get("countryCode", "UNKNOWN"),
                "score": payload.get("abuseConfidenceScore", 0),
                "incidents": payload.get("totalReports", 0)
            }
        else:
            print(f"[!] Target {ip} lookup failed. Status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as err:
        print(f"[-] Network connection timeout or routing failure for {ip}: {err}")
        return None

def export_metrics(records, destination):
    schema = ["IP Address", "Country Code", "Abuse Score %", "Total Reports", "Mitigation Status"]
    with open(destination, "w", newline="", encoding="utf-8") as out:
        writer = csv.writer(out)
        writer.writerow(schema)
        for row in records:
            status = "BLOCKED" if row["score"] > 50 else "MONITORING"
            writer.writerow([row["ip"], row["country"], row["score"], row["incidents"], status])

def main():
    if not API_KEY:
        print("[-] Configuration Error: ABUSEIPDB_API_KEY environment variable is missing.")
        return

    print(f"[*] Ingesting telemetry data from: {LOG_FILE}")
    suspicious_ips = parse_failed_logins(LOG_FILE)
    
    if not suspicious_ips:
        print("[*] Processing complete. No critical markers extracted.")
        return

    print(f"[+] Isolated {len(suspicious_ips)} unique attack sources. Commencing threat enrichment...")
    enriched_dataset = []

    for idx, ip in enumerate(suspicious_ips, 1):
        print(f"[{idx}/{len(suspicious_ips)}] Evaluating reputation metrics for: {ip}")
        time.sleep(1)
        
        telemetry = query_threat_reputation(ip, API_KEY)
        if telemetry:
            enriched_dataset.append(telemetry)

    if enriched_dataset:
        print(f"[*] Compiling indicators. Generating matrix artifact at: {OUTPUT_FILE}")
        export_metrics(enriched_dataset, OUTPUT_FILE)
        print("[+] Automation pipeline completed successfully.")
    else:
        print("[-] Data enrichment yield was zero. File compilation skipped.")

if __name__ == "__main__":
    main()
