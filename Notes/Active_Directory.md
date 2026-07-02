## Active Directory (AD)
- Microsoft's directory service for centralized identity and access management.
- Stores users, groups, computers, OUs, and Group Policies.
- Think of it as the organization's identity database.

---

## Windows Server vs Domain Controller

**Windows Server**
- Operating System.

**Domain Controller (DC)**
- A Windows Server promoted to run Active Directory Domain Services (AD DS).
- Authenticates users and manages the domain.

```
Windows Server
      │
Install AD DS
      │
Promote Server
      ▼
Domain Controller
```

---

## AD vs DC

| Active Directory | Domain Controller |
|-----------------|-------------------|
| Stores identities | Authenticates identities |
| Directory service | Server running AD DS |
| Database of objects | Uses AD to verify users |

Analogy

```
Database  → AD
Backend   → DC
```

---

## Authentication Flow

```
User
   │
Password
   ▼
Domain Controller
   │
Checks Active Directory
   ▼
Issues Kerberos Ticket
   ▼
Access File Server / Printer / SQL / Outlook
```

Password is verified once.
Services trust the Kerberos ticket.

---

## Kerberos

- Default authentication protocol in Active Directory.
- Uses tickets instead of repeatedly sending passwords.
- Enables Single Sign-On (SSO).

Password ≠ Ticket

- Password → Secret credential
- Ticket → Temporary proof that authentication already happened

JWT analogy:

```
Password → Login → JWT → API Requests
```

Kerberos Ticket works similarly.

---

## Common AD Objects

**User** → Person

**Group** → Collection of users

**Computer** → Domain-joined machine

**OU** → Logical container for organizing objects

**GPO** → Rules applied to users/computers

Examples:
- Password Policy
- Disable USB
- Lock Screen Timeout

---

## Domain

Logical boundary containing users, computers and policies.

Example:

```
corp.local
```

---

## Forest

Highest-level AD structure.
Contains one or more domains.

---

## Tree

Collection of related domains inside a forest.

---

## Kerberos vs NTLM

| Kerberos | NTLM |
|-----------|------|
| Default | Legacy |
| Ticket-based | Challenge-response |
| More secure | Less secure |

---

## Quick Revision

✔ AD = Identity database

✔ DC = Windows Server running AD DS

✔ Password verified once

✔ Kerberos issues ticket

✔ Ticket used for subsequent authentication

✔ OU organizes objects

✔ GPO applies policies

✔ Domain → Tree → Forest

<img width="940" height="1345" alt="image" src="https://github.com/user-attachments/assets/fba12514-df06-4b26-b7ec-897e01d55def" />
