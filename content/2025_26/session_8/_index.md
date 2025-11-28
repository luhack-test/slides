---
title: "Week 8: Securing the Net"
author: Aaron Kelly
date: 2025-11-28
layout: single
---

Resources:

[Cheat Sheet](./network-security-session-cheat-sheet)

[Spec](./rusty-nails-ltd-spec)

---

# Intro to Network Security

---

# Life of a Packet

![](./images/life_of_a_packet.jpg)

---

# Devices being used

Firewall

Router

Switch

---

# VLANs

- VLANs are network configs to break larger networks into virtually separate networks
- They are configured at the switch level

# VLAN ids and security

- VLANs are identified by a number
- VLANs are not secure by themselves (as they can be spoofed)
- But on trusted network segments they can be used to segregate traffic
- You should put untrusted devices on ports assigned to a VLAN (not using the VLAN tag)

---

# Subnets

Subnets are segments of larger networks

CIDR IP: 10.0.0.1/8

Subnet: 255.0.0.0

Includes all addresses from 10.0.0.0 to 10.255.255.255

---

or

CIDR IP: 192.168.1.1/25

Subnet: 255.255.255.128
Binary subnet: 11111111 11111111 11111111 10000000

Includes all addresses from 192.168.1.0 to 192.168.1.127

---

# Remember

All issues with networks can be traced back to layer 8

---

# Demo

I'm going to show you how to set up a switch and a firewall, these bits are going to be important. 

---

## luhack.uk/w8
## session.luhack.uk
