---
title: "Week 17: Metasploit"
author: LUHack
date: 2026-02-27
layout: single
---

# Metasploit

---

# What is Metasploit?

- Offensive security automation tool
- Fully open source
- Tries to guarantee reliability and trustworthiness of exploits
- Targeted towards red teamers/pentesters

---

# Pitfalls

- Limited real-world utility
- Bad reputation due to abuse by script kiddies
- Mostly written in Ruby
- It can be quite slow

---

# How it can be useful

- As part of pentests that are fully automated
- When used with automation tools such as Pymetasploit3
- Particularly useful for remote code execution attacks that are widely exploitable

---

# How it works

- A git repo full of Python/Ruby scripts that are organised into folders
- Set a couple of options interactively and then run it

---

# Prerequisite: "The Terminal"

- NOT scary
- NOT complicated
- NOT all the same

---

| The Terminal      | T'Internet  |
|-------------------|-------------|
| terminal prompt   | website     |
| terminal emulator | web browser |

---

# Demo

```
ansible@debian:/session$ exit
logout
Connection to 192.168.0.4 closed.
iron ~/f/lancs/luhack/chonk-deploy master! > sh
$ bash
iron ~/f/lancs/luhack/chonk-deploy master! > node
Welcome to Node.js v20.11.1.
Type ".help" for more information.
>
iron ~/f/lancs/luhack/chonk-deploy master! > python
Python 3.11.2 (main, Nov 30 2024, 21:22:50) [GCC 12.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
iron ~/f/lancs/luhack/chonk-deploy master! > sh
$ ssh ansible@chonk
Last login: Fri Feb  7 12:35:06 GMT 2025 from 100.84.145.21 on pts/0
ansible@luhack-big-chonk:~$ ^C
ansible@luhack-big-chonk:~$
logout
Connection to chonk closed.
$
iron ~/f/lancs/luhack/chonk-deploy master! >
```

---

# Examples of prompts

- Bash
- Powershell
- Python IDLE
- CMD

---

# Metasploit commands

There are many, but the commands that you will probably need today are:

```
$ msfconsole
$ msfvenom
```

---

# msfconsole

The main Metasploit console

---

# msfvenom

A tool for generating payloads.

---

# Meterpreter

A payload that is used to control a compromised system.

AKA a fancy bash shell

---

# Example usage

---

# Finding exploits

```
msf > search foo
```

---

# Running an exploit

```
msf > use exploit/linux/http/ivanti_connect_secure_rce_cve_2023_46805
msf exploit(ivanti_connect_secure_rce_cve_2023_46805) > show targets
    ...targets...
msf exploit(ivanti_connect_secure_rce_cve_2023_46805) > set TARGET < target-id >
msf exploit(ivanti_connect_secure_rce_cve_2023_46805) > show options
    ...show and set options...
msf exploit(ivanti_connect_secure_rce_cve_2023_46805) > exploit
```

---

# Payloads

- Single - A payload that connects back to the attacker and executes in one step.
- Stage - A smaller payload that sets up a connection and downloads a larger payload (the stager).
- Stager - The initial part of a multi-stage payload that establishes a communication channel before the main payload is
  delivered.

Note: Meterpreter is currently not working on the VM so you will need to use alternative payloads.

---

# Summary

Metasploit is a useful tool for learning how to exploit vulnerable machines and for doing automated pen tests.

---

# luhack.uk/w17
