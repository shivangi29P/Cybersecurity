# Threat Intelligence Automation Pipeline

An automated log ingestion and indicator enrichment engine that isolates malicious access vectors, cross-references signatures against global threat actors, and outputs structured intelligence data sheets.

## Architecture & Workflow

1. **Ingestion Platform:** Processes high-volume server authentication logs line-by-line.
2. **Text Parsing Engine:** Implements specific Regular Expression footprints to strip out noise fields and extract unique, deduplicated remote IP addresses.
3. **API Integration Matrix:** Queries external threat data gateways (`AbuseIPDB`) to evaluate global abuse scores and geographic parameters.
4. **Rate Limiting Middleware:** Implements dynamic execution cool-downs to prevent network throttling and connection drops.
5. **Data Export Layer:** Compiles runtime intelligence matrices into production-grade CSV files mapped to standard mitigation thresholds.

### Note: 
Require a target `enterprise_auth.log` data target inside the local system
