Interactive Cryptography Message Encryption and Decryption Application

Project Overview
This project is a Python-based application that demonstrates how cryptographic algorithms are used to encrypt and decrypt messages. It provides a simple graphical user interface that allows users to experiment with different encryption techniques.

The aim of the application is to give a practical understanding of how encryption works in real-world systems.

Features
- Encrypt and decrypt messages
- Supports multiple algorithms:
  - Caesar Cipher
  - Vigenère Cipher
  - AES (Advanced Encryption Standard)
  - RSA Algorithm
- User-friendly graphical interface (Tkinter)
- Input validation and error handling
- AES key generation and usage
- Responsive GUI design

Technologies Used
- Python
- Tkinter (GUI)
- PyCryptodome (for AES encryption)

Project Structure
crypto-app/
|-- main.py
|
|-- crypto/
| |-- caesar.py
| |-- vigenere.py
| |-- aes_crypto.py
| |-- rsa_crypto.py
|
|-- README.md


Installation and Setup

1. Clone the repository
git clone https://github.com/abdulkariimu2024/crypto-app.git
cd crypto-app

2. Create virtual environment (recommended)
python -m venv venv
venv\Scripts\activate

3. Install dependencies
pip install pycryptodome

4. Then run the application

python main.py

Usage
1. Enter a message
2. Select an encryption algorithm
3. Enter a key (if required)
4. Click Encrypt or Decrypt
5. View the output

Notes
AES encryption generates a key which must be used for decryption. The key must be saved to decrypt the message.
RSA keys are generated automatically during encryption
Classical algorithms are for demonstration purposes only

References
Anderson, R. (2020). Security engineering: A guide to building dependable distributed systems (3rd ed.). Wiley.
Menezes, A., van Oorschot, P., & Vanstone, S. (2018). Handbook of applied cryptography. CRC Press.
Stallings, W. (2017). Cryptography and network security: Principles and practice (7th ed.). Pearson.

Author
Abdul Kariimu Ggubya
BSc Computer Science
Unicaf University
