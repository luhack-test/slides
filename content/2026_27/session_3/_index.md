---
title: Scripting
layout: single
---

[//]: # (this is a slide deck introducing the concept of scripting, in particular to do fuzzing, page traversal and scraping, bruteforce logins)

# Scripting

---

## Why?

- Automation
- Repetition
- Speed
- Consistency
- Scale

---

## Scripting Vs Programming

- Rough and ready
- Only needs to work a few times
- Not necessarily maintainable
- Not necessarily readable

---

## Python Requests

- The best way to run scripts against HTTP endpoints
- Can be used to scrape, fuzz, brute force, etc.
- [Documentation](https://docs.python-requests.org/en/master/)
- [PyPi](https://pypi.org/project/requests/)

---

## Simple Example

```python
import requests

response = requests.get("https://google.com")
print(response.status_code)
print(response.text)
```

---

## BeautifulSoup

- A library for parsing HTML and XML
- [Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [PyPi](https://pypi.org/project/beautifulsoup4/)

---

## Simple Example


```python
from bs4 import BeautifulSoup

html = response.text

soup = BeautifulSoup(html, "html.parser")
divs = soup.find_all("div")

print(len(divs))

```

---

## sitemap.xml

- An XML file listing a site's pages
- Usually found at `/sitemap.xml`
- Helps search engines discover and index content
- Can include last-modified dates and priorities
- Useful for recon: a quick map of the site's pages without crawling

---

## robots.txt

- A plain text file at `/robots.txt`
- Tells crawlers which paths they should and shouldn't visit
- Uses `User-agent`, `Allow` and `Disallow` rules
- Purely advisory, so nothing enforces it
- Companies sometimes list paths they don't want search engines picking up, such as admin panels, staging areas and backups
- Useful for recon because it can point you straight at the interesting paths

---


# luhack.uk/w3
# notwordpress.luhack.uk
