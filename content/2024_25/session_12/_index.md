---
title: "Recon"
layout: single
---

# Doing Recon

---

# What is recon?

Recon is the skill of gathering information

Today we will cover active reconnaissance.

---

# What does active recon mean?

Great question

---

# Active Reconnaissance

Gaining information about a system through interaction.

This could be:

- Port Scanning
- Physical site investigations
- Interacting with a human target

---

# Quick fire networking

---

# IP Addressing

IPv4 vs IPv6

Public vs Private

---

# Network Protocols

TCP

UDP

QUIC

---

# What is NMap?

Network Mapping tool

Allows a user to scan an IP Address.

More available at nmap.org

---

# How do I get NMap?

Linux: Either already installed or likely available in your package manager of choice.

Windows: Can be installed in Windows, but we'd recommend either hosting a Kali/Parrot VM or install Kali through WSL.

MacOS/OSX: Install from nmap.org/download

Available on BSD, Solaris, Amiga etc.

---

# Common Uses of NMap

To find:

- What ports are open on an IP Address?
- What protocols are running?
- Detect an Operating System

---

# Parameters

-sS for SYN

-sT for Connect

-sU for UDP

-A for OS and service Detection

---

# Port Specific

-p 443

-p 1-100

-p- for all ports

---

# NMap with Scripts

NMap also allows you to pass in scripts to make the tool even more powerful.

---

# Curl

Curl is a tool used to transfer data to and from a server by passing in a URL. 

---

# FTP

The File Transfer Protocol

---

# Dig

Allows you to get the DNS records for servers when you know the domain name or IP address

---

# Netcat

This is a tool that allows you to write data through TCP or UDP across a network

---

# Le Google

Allows you to search for things like protocols you've never heard of look up CVEs that may be useful/search if there are any CVEs within protocols you can take advantage of.

---

# SSH

Secure Shell is command that allows you to remotely access the device attached to an IP address if it has been enabled

---

# This very specific command

openssl s_client -connect www.example.com:443 </dev/null 2>/dev/null | openssl x509 -inform pem -text

---

luhack.uk/w13
