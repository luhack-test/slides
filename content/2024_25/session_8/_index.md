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

# luhack.uk/w8
