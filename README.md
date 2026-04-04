# Interactive Cryptography Message Encryption and Decryption Application

## Overview
This project is a Python-based application that demonstrates how cryptographic algorithms are used to encrypt and decrypt messages. It provides a simple graphical user interface that allows users to experiment with different encryption techniques.

## Features
- Encrypt and decrypt messages
- Supports multiple algorithms:
  - Caesar Cipher
  - Vigenère Cipher
  - AES (Advanced Encryption Standard)
- User-friendly graphical interface (Tkinter)

## Technologies Used
- Python
- Tkinter (GUI)
- PyCryptodome (for AES encryption)

## Project Structure
crypto-app/
│── main.py
│── crypto/
│ ├── caesar.py
│ ├── vigenere.py
│ ├── aes_crypto.py
│── README.md


## Installation
1. Clone the repository:
Go to bash
git clone https://github.com/your-username/crypto-app.git

# Install pycryptodome with the command below
pip install pycryptodome

# THen run the application
python main.py

## Usage
1. Enter a message
2. Select an encryption algorithm
3. Enter a key (if required)
4. Click Encrypt or Decrypt

## Notes
AES generates a random key during encryption. The key must be saved to decrypt the message.
