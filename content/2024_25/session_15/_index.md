---
title: "Linux Exploitation"
layout: single
---

# Linux Exploitation

---

The goal on compromising a Linux machine is to escalate privileges to root or pivot to other machines on the network.

---

# Some useful info

---

## Cron

- A time-based job scheduler in Unix-like operating systems
- Executes commands at specified dates and times
- Runs them as the user who scheduled the job

---

Schedule strings are in the format:

```
* * * * * command to be executed
```

---

Where the fields are:

- minute (0 - 59)
- hour (0 - 23)
- day of month (1 - 31)
- month (1 - 12)
- day of week (0 - 6) (Sunday to Saturday)
- command to be executed

---

## $PATH

- A list of directories that the shell searches for executables
- The order of directories is important
- Can get the current value with `echo $PATH`

---

## `which`

- A command that returns the path of the executable that would be executed in the current environment
- Can be used to check if a command is in the $PATH

--- 

## Envriorment Variables

- Variables that are set in the shell
- Can be used to change the behaviour of programs
- can be set for the shell with `export VAR=value`
- Can be set for a single command with `VAR=value command`

---

## Linux File Permissions

- who—identities ie. users/groups
- what—read, write, execute

---

```bash
$ ls -la .bashrc
-rw-r--r-- 1 max max 2757 Dec 25 23:36 .bashrc
```

---

## -rw-r-x---

In the format  

```
{file type}{owner permissions}{group permissions}{other permissions}
```

---

## Numeric Permissions

- Read: 4
- Write: 2
- Execute: 1
- No permissions: 0

Therfore, `rwxr-x---` would be `750`

---

## SUID/SGID

- Set User ID
- When set, the program is run with the privileges of the owner of the file

`-rwsr-xr-x`

---

## Shared Objects

- `.so` files
- Can be loaded into a process at runtime
