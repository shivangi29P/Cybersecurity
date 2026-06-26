# Linux SSH Authentication & Log Analysis

## Overview

This project focuses on SSH authentication monitoring and Linux log analysis using Ubuntu and Kali Linux in a controlled lab environment. Authentication events, user activity, and privileged operations were investigated through system logs.

        Kali Linux (SSH Client)
                 │
                 │ SSH Authentication
                 ▼
        Ubuntu Linux Server
      ┌─────────────────────────┐
      │ OpenSSH Service (sshd)  │
      └─────────────────────────┘
                 │
                 ▼
      Linux Authentication Logs
         (/var/log/auth.log)
                 │
                 ▼
      ┌─────────────────────────┐
      │ Linux Log Investigation │
      └─────────────────────────┘
                 │
                 ▼
      Authentication Investigation

## Lab Environment

| Component  | Details                     |
| ---------- | --------------------------- |
| Client     | Kali Linux                  |
| Server     | Ubuntu                      |
| Service    | OpenSSH                     |
| Log Source | `/var/log/auth.log`         |
| Network    | VirtualBox Internal Network |

## Activities Performed

* Configured SSH communication between systems
* Verified network connectivity
* Performed port scanning using Nmap
* Generated failed and successful SSH logins
* Reviewed local user accounts
* Created a new user account
* Investigated sudo activity
* Analyzed authentication logs

## Key Findings

* Failed and successful SSH logins were successfully recorded.
* Authentication events were traced to the source host.
* Administrative actions generated auditable sudo logs.
* Authentication logs provided visibility into user activity and access patterns.

## Skills Demonstrated

* SSH Configuration
* Authentication Monitoring
* Log Analysis
* Security Investigation
* Network Troubleshooting

