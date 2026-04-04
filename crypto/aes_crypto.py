from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64


def pad(text):
    while len(text) % 16 != 0:
        text += ' '
    return text


def encrypt_aes(text):
    key = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_ECB)

    padded_text = pad(text)
    encrypted_bytes = cipher.encrypt(padded_text.encode())

    return base64.b64encode(encrypted_bytes).decode(), key


def decrypt_aes(cipher_text, key):
    cipher = AES.new(key, AES.MODE_ECB)
    decoded = base64.b64decode(cipher_text)
    decrypted = cipher.decrypt(decoded)

    return decrypted.decode().strip()