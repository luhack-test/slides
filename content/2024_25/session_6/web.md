---
---

# Web Exploitation

Isaac's idea of a great afternoon

---

# Types of Web Attack

- Brute Force
- Command Injection
- File Upload
- SQL Injection
- Cross Site Scripting

---

# Other web stuff to be aware of

robots.txt

security.txt

---

# Brute Force

Hydra is capable of taking file inputs as dictionaries to attack login pages.

```bash
hydra -l <username> -P <path_to_passwords.txt> <target_url> http-post-form "<login_form_action>:<username_field>=^USER^&<password_field>=^PASS^:F=incorrect"
```

---

# Command Injection

Vulnerable PHP can allow for you to write commands into the PHP script of a website and then execute that code.

---

# File upload

When a website allows you to upload an image, you don't have to upload an image ...

You could instead upload a script that does something else.

---

# SQL Injection

![xkcd meme](../img/Bobby.png)

---

Failure to santise your SQL searches can result in someone doing.

You are presented with a username box. You can either type a username or the User ID in the database if you know it. 

Alternatively, you could type any number and if there is a username attached to that ID number, you will then be prompted to sign in as that user.

Then with a dictionary attack, you can find out that user 42069's password is Password1.

This can also be automated with a tool like SQLmap.

