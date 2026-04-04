import tkinter as tk
from tkinter import ttk

from crypto.caesar import encrypt_caesar, decrypt_caesar
from crypto.vigenere import encrypt_vigenere, decrypt_vigenere
from crypto.aes_crypto import encrypt_aes, decrypt_aes


def encrypt():
    text = input_text.get("1.0", tk.END).strip()
    algo = algorithm.get()

    if algo == "Caesar":
        result = encrypt_caesar(text, int(key_entry.get()))
    elif algo == "Vigenere":
        result = encrypt_vigenere(text, key_entry.get())
    elif algo == "AES":
        result, aes_key.set(encrypt_aes(text))
    else:
        result = "Select Algorithm"

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result)


def decrypt():
    text = input_text.get("1.0", tk.END).strip()
    algo = algorithm.get()

    if algo == "Caesar":
        result = decrypt_caesar(text, int(key_entry.get()))
    elif algo == "Vigenere":
        result = decrypt_vigenere(text, key_entry.get())
    elif algo == "AES":
        result = decrypt_aes(text, aes_key.get())
    else:
        result = "Select Algorithm"

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result)


# GUI
root = tk.Tk()
root.title("Cryptography App")

algorithm = tk.StringVar()
aes_key = tk.StringVar()

ttk.Label(root, text="Enter Message:").pack()
input_text = tk.Text(root, height=5)
input_text.pack()

ttk.Label(root, text="Select Algorithm:").pack()
algo_box = ttk.Combobox(root, textvariable=algorithm)
algo_box['values'] = ("Caesar", "Vigenere", "AES")
algo_box.pack()

ttk.Label(root, text="Enter Key:").pack()
key_entry = ttk.Entry(root)
key_entry.pack()

ttk.Button(root, text="Encrypt", command=encrypt).pack()
ttk.Button(root, text="Decrypt", command=decrypt).pack()

output_text = tk.Text(root, height=5)
output_text.pack()

root.mainloop()