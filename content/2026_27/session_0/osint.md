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

    img.portrait {
        aspect-ratio: auto;
        width: auto;
    }
</style>

# Open Source Intelligence

<img id="title-image" src="../img/osint.png">

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

![](../img/luhack-archive.png)

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

![](../img/uni-income.png)

---

# Google Dorking

A way of searching Google with advanced/specific operators to discover hard to find information.

![](../img/google-dorking.png)

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

![](../img/dig-lancs-spf.png)
![](../img/google-lancs-spf.png)

---

# Compsoc x FemTech Freshers Event

<img class="portrait" src="../img/compsoc-event.png">

---

# [luhack.uk/w0](https://luhack.uk/w0)

Domain Dossier: https://centralops.net/co/DomainDossier

DNS Records: https://dnsdumpster.com/

The Wayback Machine: https://web.archive.org/

Certificate Transparency Log: https://crt.sh/

Google Dorking Cheatsheet: https://gist.github.com/sundowndev/283efaddbcf896ab405488330d1bbc06

Online Dig Tool: https://toolbox.googleapps.com/apps/dig/

https://dnsdumpster.com/
