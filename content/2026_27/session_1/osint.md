---
title: "Open Source Intelligence"
layout: single
author: "Luke Needle & Kristófer Antonsson"
date: 2026-10-02
---

<style>
    img {
        width: 80%;
    }

    img#title-image {
        width: 60%;
        max-height: initial;
    }
</style>

# Open Source Intelligence

<img id="title-image" src="../img/osint.png" alt="alt text">

---

# What is Open Source Intelligence?

Passive reconnaissance, using publicly available information to gather intel without alerting your target.

Allows you to build a clearer picture of a company, system, event, or location.

Typically involves search engines, public company records, DNS records, and archived websites.

---

# Whois

WHOIS records are public registration records for domain names and IP address ranges.

Often includes IT Administrator contacts.

https://centralops.net/co/DomainDossier

`$ whois`

---

# Public Archives

Public digital library of websites and historical snapshots.

![alt text](../img/luhack-archive.png)

https://web.archive.org/

---

# Certificates

Certificate authorities (CAs) records all SSL certificates issued on an immutable public ledger.

Useful for finding subdomains (including old subdomains... Wayback machine 👀)

https://crt.sh/

---

# Public Company Records

UK companies are publicly registered on companies house.

You can find information such as, directors names & addresses, yearly profit, number of employees, and amount of assets held.

![alt text](../img/uni-income.png)

---

# Google Dorking

A way of searching Google with advanced/specific operators to discover hard to find information.

![alt text](../img/google-dorking.png)

https://gist.github.com/sundowndev/283efaddbcf896ab405488330d1bbc06

---

# DNS Records

A DNS record tells a client where to locate systems.

https://toolbox.googleapps.com/apps/dig/

https://dnsdumpster.com/

https://bgp.tools/

`$ dig`

---

# SPF Records

Tells a receiving mail server the authorised IP addresses and what to do with mail from unauthorised senders.

- Soft-fail (~all) - Mark unauthorised mail as suspicious
- Hard-fail (-all) - Reject unauthorised mail
- Neutral response (?all) - Ignore the record

---

# Neutral responses are not secure

![alt text](../img/dig-lancs-spf.png)
![alt text](../img/google-lancs-spf.png)

---

# Compsoc Freshers Event

- CompSoc x FemTech Welcome Talk
- Monday 5th October at 6PM
- Bowland Main LT
- Learn about the societies and the executive committees
- Pizza is included!

https://www.instagram.com/lucompsoc/

---

# [luhack.uk/w1](https://luhack.uk/w1)

Domain Dossier: https://centralops.net/co/DomainDossier

DNS Records: https://dnsdumpster.com/

The Wayback Machine: https://web.archive.org/

Certificate Transparency Log: https://crt.sh/

Google Dorking Cheatsheet: https://gist.github.com/sundowndev/283efaddbcf896ab405488330d1bbc06

Online Dig Tool: https://toolbox.googleapps.com/apps/dig/

https://dnsdumpster.com/
