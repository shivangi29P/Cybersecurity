# Log Parser Studio Analysis

## Overview

This project demonstrates security log investigation using Log Parser Studio and SQL-style queries against exported Windows Security Logs.

             Windows Security Logs (.evtx)
                         │
                         ▼
         Export Windows Security Event Logs
                         │
                         ▼
          Log Parser Studio Analysis Engine
       ┌────────────────────────────────────┐
       │ SQL-like Query Processing          │
       │ • Filtering                        │
       │ • Searching                        │
       │ • Event Aggregation                │
       │ • Statistical Analysis             │
       └────────────────────────────────────┘
                         │
                         ▼
             Investigation & Reporting
             
## Objectives

- Import Security Logs into Log Parser Studio
- Query Windows Event Data
- Perform event frequency analysis
- Investigate authentication activity
- Analyze privilege assignment events
- Review credential-related events

