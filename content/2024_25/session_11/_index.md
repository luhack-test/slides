---
title: Hacking Military Grade Encryption
layout: single
---

# Hacking Military Grade Encryption

![ECB](https://github.com/pakesson/diy-ecb-penguin/blob/master/Tux_ecb.png?raw=true)

---

## Terms of reference

- Plaintext: The original data
- Ciphertext: The encrypted data
- Key: The secret used to encrypt and decrypt the data
- Encryption: The process of converting plaintext to ciphertext
- Encoding: The process of changing the format of data, e.g. binary to hexadecimal

---

## A good cyphertext

- Looks like random data
- Has good confusion and diffusion

---

## Confusion

- The relationship between the key and the cyphertext should be complex
- Changing one bit of the key should change the cyphertext completely

---

## Diffusion

- The relationship between the plaintext and the cyphertext should be complex
- Changing one bit of the plaintext should change the cyphertext completely

---

## What is AES and why am I calling it Military Grade?

- AES = Advanced Encryption Standard
- Symmetric encryption algorithm
- Used by US government to protect classified information, hence "Military Grade"

---

## What actually is AES?

- Block cypher
- Operates on 128-bit blocks
- Key lengths of 128, 192, or 256 bits
- AKA Rijndael, a portmanteau of the inventors' names

---

## What is a block cypher?

- A block cypher is an algorithm that encrypts data in fixed-size blocks
- Unlike a stream cypher, which encrypts data bit by bit

---

## How does AES work?

- AES operates on a 4x4 matrix of bytes
- The matrix is transformed by a series of operations
- The operations are repeated for a number of rounds, depending on the key length
- The final matrix is the encrypted data

---

## Round Keys

- The key is expanded into a series of round keys
- This prevents slide attacks

---

![AES Flow Chat](./aes-flow-chart.png)

---

## What if I want to encrypt more than 128 bits?

- There are several ways to do this (these are called modes of operation)
    - ECB (Electronic Code Book)
    - CBC (Cipher Block Chaining)
    - CRT (Counter)

---

## ECB

- The simplest mode of operation
- Each block is encrypted independently

---

![ECB](./ecb.png)

---

## Why is ECB bad?

- Identical plaintext blocks will encrypt to identical ciphertext blocks
- This leaks information about the plaintext
- It has poor diffusion, as you can change one block of the plaintext and see the change in only one block of the
  cyphertext
- But it does have good confusion because it is using AES

---

## So, WTF is the ECB Penguin?

---

![Tux](https://github.com/pakesson/diy-ecb-penguin/blob/master/Tux.png?raw=true)

---

![ECB](https://github.com/pakesson/diy-ecb-penguin/blob/master/Tux_ecb.png?raw=true)

---

## CBC

- Each block is XORed with the previous block before encryption
- The first block is XORed with an IV (Initialisation Vector)
- This prevents identical plaintext blocks from encrypting to identical ciphertext blocks
- It has good diffusion and confusion, as long as the IV is random and unique

## IV

- The IV should be random
- The IV should be unique for each message
- The IV does not need to be secret, and normally is sent with the message

---

![CBC](./cbc.png)

---

## CRT

- Converts AES to a stream cypher
- Combines a nonce and a counter to create a unique key for each block
- The nonce is a random number and MUST be unique for each message
- The counter is incremented for each block, creating diffusion
- The key is XORed with the plaintext to create the cyphertext

---

![CRT](./ctr.png)

---

You can find an example of the three modes discussed [here](./modes-demo.py)

---

# luhack.uk/w11

