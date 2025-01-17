---
layout: single
title: Modes of Operation Demo
---

# Modes of Operation Demo

```python
class MockBlockCipher:
    def __init__(self, key):
        self.key = key

    @staticmethod
    def _pad(data):
        """Pad the data to make its length a multiple of 8."""
        while len(data) % 8 != 0:
            data += ' '
        return data

    @staticmethod
    def _unpad(data):
        """Remove padding from the data."""
        return data.rstrip()

    def encrypt(self, plaintext):
        """Encrypt the plaintext using a simple mock block cipher."""
        padded_plaintext = self._pad(plaintext)
        ciphertext = ''

        for char in padded_plaintext:
            # Simple transformation: shift character by the key's length
            encrypted_char = chr((ord(char) + len(self.key)) % 256)
            ciphertext += encrypted_char

        return ciphertext

    def decrypt(self, ciphertext):
        """Decrypt the ciphertext back to plaintext."""
        decrypted_text = ''

        for char in ciphertext:
            # Reverse the transformation: shift character back by the key's
            # length
            decrypted_char = chr((ord(char) - len(self.key)) % 256)
            decrypted_text += decrypted_char

        return self._unpad(decrypted_text)


def xor(a, b):
    return ''.join(chr(ord(x) ^ ord(y)) for x, y in zip(a, b))


def ecb_encrypt(plaintext, key):
    # Split the plaintext into 8-byte blocks
    plaintext_blocks = []
    for i in range(0, len(plaintext), 8):
        plaintext_blocks.append(plaintext[i:i + 8])

    # Encrypt each block separately
    cyphertext_blocks = []
    for block in plaintext_blocks:
        # NOTE: I do not care about any block apart from the one I am
        # encrypting.
        cyphertext_blocks.append(MockBlockCipher(key).encrypt(block))

    # Concatenate the encrypted blocks
    return ''.join(cyphertext_blocks)


def ecb_decrypt(ciphertext, key):
    # Split the ciphertext into 8-byte blocks
    ciphertext_blocks = []
    for i in range(0, len(ciphertext), 8):
        ciphertext_blocks.append(ciphertext[i:i + 8])

    # Decrypt each block separately
    plaintext_blocks = []
    for block in ciphertext_blocks:
        plaintext_blocks.append(MockBlockCipher(key).decrypt(block))

    # Concatenate the decrypted blocks
    return ''.join(plaintext_blocks)


def cbc_encrypt(plaintext, key, iv):
    # Split the plaintext into 8-byte blocks
    plaintext_blocks = []
    for i in range(0, len(plaintext), 8):
        plaintext_blocks.append(plaintext[i:i + 8])

    # Encrypt each block separately, chaining the previous block's
    # cyphertext with the current block's plaintext.
    cyphertext_blocks = []
    previous_block = iv
    for block in plaintext_blocks:
        # NOTE: I xor the current block with the previous block so that
        # the same plaintext block does not always encrypt to the same
        # cyphertext block.
        block = xor(block, previous_block)
        cyphertext_blocks.append(MockBlockCipher(key).encrypt(block))
        previous_block = cyphertext_blocks[-1]

    return ''.join(cyphertext_blocks)


def cbc_decrypt(ciphertext, key, iv):
    # Split the ciphertext into 8-byte blocks
    ciphertext_blocks = []
    for i in range(0, len(ciphertext), 8):
        ciphertext_blocks.append(ciphertext[i:i + 8])

    # Decrypt each block separately, chaining the previous block's
    # cyphertext with the current block's plaintext.
    plaintext_blocks = []
    previous_block = iv
    for block in ciphertext_blocks:
        decrypted_block = MockBlockCipher(key).decrypt(block)
        plaintext_blocks.append(xor(decrypted_block, previous_block))
        previous_block = block

    # Concatenate the decrypted blocks
    return ''.join(plaintext_blocks)


def ctr(plaintext, key, nonce):
    # Split the plaintext into 8-byte blocks
    plaintext_blocks = []
    for i in range(0, len(plaintext), 8):
        plaintext_blocks.append(plaintext[i:i + 8])

    cyphertext_blocks = []
    for counter, block in enumerate(plaintext_blocks):
        # NOTE: I use the nonce and the block's index to generate the
        # counter_nonce. This ensures that the same plaintext block does
        # not always encrypt to the same cyphertext block.

        counter_nonce = nonce + counter

        # Encrypt the counter_nonce to generate the keystream
        keystream = MockBlockCipher(key).encrypt(chr(counter_nonce))

        # XOR the block with the keystream
        cyphertext_blocks.append(xor(block, keystream))

    # Concatenate the encrypted blocks
    return ''.join(cyphertext_blocks)


def example():
    # The key is the secret bit that you do not want to share with anyone.
    # (Much like a physical key for a lock.)
    key = 'abc123'

    # The IV (initialization vector) is a random value that you need to
    # generate for each encryption. Used in CBC mode. It is sent along with
    # the ciphertext.
    iv = 'def456'

    # The nonce (number used once) is a number that is used per encryption.
    # It is sent along with the ciphertext. It is used in CTR mode.
    # If you generate it randomly, your random number must be big enough
    # that you do not repeat the same number in the future.
    nonce = 0

    plaintext = 'Hello, world!'
    print('Plaintext:', plaintext)

    # ECB (Electronic Code Book) mode
    ecb_encrypted = ecb_encrypt(plaintext, key)
    ecb_decrypted = ecb_decrypt(ecb_encrypted, key)

    print('ECB encrypted:', ecb_encrypted)
    print('ECB decrypted:', ecb_decrypted)

    # CBC (Cipher Block Chaining) mode
    cbc_encrypted = cbc_encrypt(plaintext, key, iv)
    cbc_decrypted = cbc_decrypt(cbc_encrypted, key, iv)

    print('CBC encrypted:', cbc_encrypted)
    print('CBC decrypted:', cbc_decrypted)

    # CTR (Counter) mode
    ctr_encrypted = ctr(plaintext, key, nonce)
    ctr_decrypted = ctr(ctr_encrypted, key, nonce)

    print('CTR encrypted:', ctr_encrypted)
    print('CTR decrypted:', ctr_decrypted)


if __name__ == '__main__':
    example()
```
