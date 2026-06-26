# Splunk SSH Authentication Monitoring & Log Analysis

## Overview

This project demonstrates centralized SSH authentication monitoring using Splunk Enterprise. Authentication logs from an Ubuntu system were continuously collected, indexed, and analyzed to investigate failed login attempts, successful SSH authentications, and privileged user activity.

              Kali Linux
             (SSH Client)
                   │
      SSH Authentication Requests
                   │
                   ▼
          Ubuntu Linux Server
      ┌──────────────────────────┐
      │ OpenSSH Service (sshd)   │
      └──────────────────────────┘
                   │
                   ▼
          Authentication Logs
          (/var/log/auth.log)
                   │
        File Monitoring Input
                   │
                   ▼
      ┌──────────────────────────┐
      │ Splunk Enterprise        │
      │                          │
      │ Parsing & Indexing       │
      │ Event Storage            │
      │ Search Processing (SPL)  │
      └──────────────────────────┘
                   │
                   ▼
        Security Investigation
      ┌──────────────────────────┐
      │ Failed Logins            │
      │ Successful Logins        │
      │ Sudo Activity            │
      │ Statistics               │
      │ Time-based Visualization │
      └──────────────────────────┘

## Lab Environment

| Component | Details |
|------------|------------|
| SIEM Platform | Splunk Enterprise |
| Client System | Kali Linux |
| Server System | Ubuntu Linux |
| Service Monitored | OpenSSH |
| Log Source | `/var/log/auth.log` |
| Network | VirtualBox Internal Network |

## Activities Performed

- Installed and configured Splunk Enterprise
- Configured file monitoring for Linux authentication logs
- Verified log ingestion and indexing
- Investigated failed SSH authentication attempts
- Analyzed successful SSH logins
- Monitored sudo activity
- Performed SPL-based searches and event analysis
- Generated statistical and timeline visualizations

## Key Findings

- Multiple failed SSH login attempts were identified and traced to the source host.
- Successful authentications were correlated with previous failed login events.
- Administrative actions executed through sudo were successfully monitored.
- Splunk provided centralized visibility into authentication and privilege-related activities.
- Event correlation enabled reconstruction of the complete SSH activity timeline.

## Skills Demonstrated

- Splunk Enterprise
- Security Information and Event Management (SIEM)
- Linux Log Analysis
- SSH Authentication Monitoring
- SPL Querying
- Event Correlation
- Security Investigation
- Threat Detection Fundamentals
