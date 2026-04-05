from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64


def generate_keys():
    key = RSA.generate(2048)
    private_key = key
    public_key = key.publickey()
    return public_key, private_key


def encrypt_rsa(message, public_key):
    cipher = PKCS1_OAEP.new(public_key)
    encrypted = cipher.encrypt(message.encode())
    return base64.b64encode(encrypted).decode()


def decrypt_rsa(cipher_text, private_key):
    cipher = PKCS1_OAEP.new(private_key)
    decoded = base64.b64decode(cipher_text)
    decrypted = cipher.decrypt(decoded)
    return decrypted.decode()