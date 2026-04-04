def generate_key(text, key):
    key = list(key)
    if len(text) == len(key):
        return key
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)


def encrypt_vigenere(text, key):
    key = generate_key(text, key)
    cipher_text = []

    for i in range(len(text)):
        if text[i].isalpha():
            x = (ord(text[i].upper()) + ord(key[i].upper())) % 26
            x += ord('A')
            cipher_text.append(chr(x))
        else:
            cipher_text.append(text[i])

    return "".join(cipher_text)


def decrypt_vigenere(cipher_text, key):
    key = generate_key(cipher_text, key)
    orig_text = []

    for i in range(len(cipher_text)):
        if cipher_text[i].isalpha():
            x = (ord(cipher_text[i].upper()) - ord(key[i].upper()) + 26) % 26
            x += ord('A')
            orig_text.append(chr(x))
        else:
            orig_text.append(cipher_text[i])

    return "".join(orig_text)