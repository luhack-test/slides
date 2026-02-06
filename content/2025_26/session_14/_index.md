---
title: "Week 14: Reverse Engineering"
author: LUHack
date: 2026-02-06
layout: single
---

# luhack.uk/w14

# SQL injection 

## What is SQL Injection (SQLi)?
SQLi is a vulnerability where untrusted input is incorporated into SQL queries without proper handling, allowing an attacker to change the intended query. Consequences include data exposure, authentication bypass, and (in some databases/configs) remote code execution.

## Why it matters
- Databases hold sensitive data (users, passwords, secrets).  
- SQLi can leak or modify all data the DB user can access.  
- Some DB engines (e.g., PostgreSQL) have features (COPY TO PROGRAM, pg_read_file) that can escalate SQLi into command execution or file disclosure.

## A minimal example
Application builds a query like:
SELECT * FROM Users WHERE id = 1

If input is concatenated naively:
SELECT * FROM Users WHERE id = 1 OR 1=1
This returns all rows (authentication bypass / data leakage).

Example payloads:
- Numeric field: 1 OR 1=1
- String field: ' OR '1'='1

## Common types of SQLi
- In-band (classic)
  - Error-based
  - UNION-based (combine query results to read arbitrary columns)
- Blind
  - Boolean-based (true/false checks)
  - Time-based (sleep delays to exfiltrate data bit-by-bit)
- Out-of-band (OOB) — uses external channels if DB supports them

## Advanced techniques (brief)
- UNION SELECT to craft rows with controlled columns and read data.
- Blind extraction via boolean or time side-channels when results aren't shown.
- Using DB-specific functions/features to read files or execute commands (Postgres: COPY ... TO PROGRAM, pg_read_file).
- Automation with sqlmap to accelerate discovery and extraction.

## Quick testing checklist
1. Identify injection points (GET params, POST bodies, cookies, headers).  
2. Try simple probes:
   - `' OR '1'='1' -- ` (strings)
   - `1 OR 1=1` (numbers)
3. If response changes, narrow the payload and confirm type (in-band vs blind).  
4. For UNION-based testing, **determine column count**: `UNION SELECT NULL,NULL,...`  
5. Use time-based probes if no visible output: `'; SELECT pg_sleep(5); --` (Postgres example).  
6. Automate carefully with sqlmap or use a proxy (Burp/ZAP) to tune payloads.

## Prevention (practical)
- Use parameterized queries / prepared statements (do not concatenate user input into SQL).  
- Use an ORM or query builder that enforces parameterization where possible.  
- Enforce least-privilege on DB accounts (no superuser; restrict file/exec privileges).  
- Validate and normalize inputs (types/lengths), but don’t rely on validation as the only defense.  
- Avoid exposing detailed DB errors to users (generic errors + logging).  


## Short code example
```python
from api.db import run_query

# Vulnerable (do not use)
def get_user_vulnerable(user_id):
    sql = f"SELECT * FROM users WHERE id = {user_id}"
    return run_query(sql)

# Safe: use parameterized queries (driver-specific placeholder)
def get_user_safe(user_id):
    # Example using %s-style placeholders (psycopg2, MySQLdb)
    return run_query("SELECT * FROM users WHERE id = %s", (user_id,))

```

## Tools & references
- sqlmap — automation for detection and exploitation  
- Burp Suite / OWASP ZAP — intercepting and manipulating requests  
- OWASP SQL Injection cheat sheet: https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html  
- OWASP Top Ten: https://owasp.org/www-project-top-ten/
## Fuzzing tools & SQLi wordlists

- WFuzz SQL injection wordlist — https://github.com/xmendez/wfuzz/blob/master/wordlist/Injections/SQL.txt  
- PenTestical sqli repository — https://github.com/PenTestical/sqli


## Tips
- Treat every input as hostile.  
- Use parameterized queries always.  
- Limit DB privileges and monitor queries.  
- Test with simple probes before using automation.  
- Learn the DB-specific risks (e.g., Postgres COPY/pg_read_file).


## This weeks challenge https://session.luhack.uk/