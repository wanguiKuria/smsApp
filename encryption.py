from Crypto.Cipher import AES
import os

def generate_key():
    return os.urandom(32)

def encrypt(data, key):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(data)
    return nonce, ciphertext, tag

def decrypt(nonce, ciphertext, tag, key):
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)
    return data

# Example usage
key = generate_key()
print(f"Generated Key: {key.hex()}")

data = b"Secret message"
nonce, ciphertext, tag = encrypt(data, key)
print(f"Ciphertext: {ciphertext.hex()}")

decrypted_data = decrypt(nonce, ciphertext, tag, key)
print(f"Decrypted Data: {decrypted_data.decode()}")
