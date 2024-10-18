---
title: "Recon"
layout: single
---

# Doing Recon

Now to do some Bond stuff

---

# What is recon?

Recon is the skill of gathering information

Today we will cover active reconnaissance.

Passive reconnaissance is next week (come along, funnies will be had)

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

# What is Wireshark?

Packet analysis tool

Allows a packet to be broken down to gain a better understanding

Can be used to discern what protocols are being used to pass data between nodes

---

# How does Wireshark work?

Wireshark takes captured packets and allows you to analyse them

This can give you an indication of how things are running

Can also capture any passwords if they are sent in plaintext ...

---

