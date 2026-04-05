import tkinter as tk
from tkinter import ttk, messagebox

from crypto.caesar import encrypt_caesar, decrypt_caesar
from crypto.vigenere import encrypt_vigenere, decrypt_vigenere
from crypto.aes_crypto import encrypt_aes, decrypt_aes
from crypto.rsa_crypto import generate_keys, encrypt_rsa, decrypt_rsa

aes_key_storage = None 
rsa_public_key = None
rsa_private_key = None


def encrypt():
    global aes_key_storage
    text = input_text.get("1.0", tk.END).strip()
    algo = algorithm.get()
    key = key_entry.get().strip()

    if not text:
        messagebox.showerror("Error", "Please enter text")
        return

    try:
        if algo == "Caesar":
            if not key.isdigit():
                raise ValueError("Key must be a number")
            result = encrypt_caesar(text, int(key))

        elif algo == "Vigenere":
            if not key:
                raise ValueError("Enter a key")
            result = encrypt_vigenere(text, key)

        elif algo == "AES":
            result, aes_key_storage = encrypt_aes(text)
            aes_key_var.set(aes_key_storage)
            messagebox.showinfo("AES Key", f"Save this key: {aes_key_storage}")

        elif algo == "RSA":
            global rsa_public_key, rsa_private_key
            rsa_public_key, rsa_private_key = generate_keys()
            result = encrypt_rsa(text, rsa_public_key)

        else:
            result = "Select Algorithm"

        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, result)

    except Exception as e:
        messagebox.showerror("Error", str(e))


def decrypt():
    global aes_key_storage
    text = input_text.get("1.0", tk.END).strip()
    algo = algorithm.get()
    key = key_entry.get().strip()

    if not text:
        messagebox.showerror("Error", "Please enter text")
        return

    try:
        if algo == "Caesar":
            if not key.isdigit():
                raise ValueError("Key must be a number")
            result = decrypt_caesar(text, int(key))

        elif algo == "Vigenere":
            if not key:
                raise ValueError("Enter a key")
            result = decrypt_vigenere(text, key)

        elif algo == "AES":
            key_from_user = aes_key_var.get().strip()
            
            if not key_from_user:
                raise ValueError("Enter AES key")
            
            result = decrypt_aes(text, key_from_user)

        elif algo == "RSA":
            if rsa_private_key is None:
                raise ValueError("Encrypt first to generate RSA keys")
            result = decrypt_rsa(text, rsa_private_key)

        else:
            result = "Select Algorithm"

        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, result)

    except Exception as e:
        messagebox.showerror("Error", str(e))

def on_algo_change(event):
    if algorithm.get() in ["AES", "RSA"]:
        key_entry.config(state="disabled")
    else:
        key_entry.config(state="normal")

# Graphical User Interface
root = tk.Tk()
root.title("Cryptography Application - Abdul Kariimu")
root.minsize(600, 450)
root.geometry("650x500")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.configure(bg="#eef2f5")

style = ttk.Style()
style.configure("TLabel", background="#eef2f5", font=("Segoe UI", 10))
style.configure("TButton", font=("Segoe UI", 10))
style.configure("TCombobox", padding=5)

algorithm = tk.StringVar()
algorithm.set("Caesar")
aes_key_var = tk.StringVar()

main_frame = tk.Frame(root, bg="#eef2f5", padx=20, pady=20)
main_frame.grid(row=0, column=0, sticky="nsew")
main_frame.rowconfigure(0, weight=1)
main_frame.rowconfigure(1, weight=1)
main_frame.rowconfigure(2, weight=0)
main_frame.rowconfigure(3, weight=1)
main_frame.columnconfigure(0, weight=1)

input_frame = tk.LabelFrame(main_frame, text="Input", bg="#eef2f5", font=("Segoe UI", 10, "bold"), padx=10, pady=10)
input_frame.grid(row=0, column=0, sticky="nsew", pady=10)
input_frame.rowconfigure(1, weight=1)
input_frame.columnconfigure(0, weight=1)


tk.Label(input_frame, text="Enter Message To Encrypt Or Decrypt:", bg="#eef2f5").grid(row=0, column=0, sticky="w")
input_text = tk.Text(input_frame, height=4, width=60, bg="white")
input_text.grid(row=1, column=0, columnspan=2, sticky="nsew")

settings_frame = tk.LabelFrame(main_frame, text="Settings", bg="#eef2f5", font=("Segoe UI", 10, "bold"), padx=10, pady=10)
settings_frame.grid(row=1, column=0, sticky="nsew", pady=10)

tk.Label(settings_frame, text="Select Algorithm (From Drop down):").grid(row=0, column=0, sticky="w")

tk.Label(settings_frame, text="Enter Key (if required):").grid(row=1, column=0, sticky="w")
key_entry = ttk.Entry(settings_frame)
key_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(settings_frame, text="AES Key:").grid(row=2, column=0, sticky="w")
aes_key_entry = ttk.Entry(settings_frame, textvariable=aes_key_var, width=40)
aes_key_entry.grid(row=2, column=1, padx=5, pady=5)

algo_box = ttk.Combobox(settings_frame, textvariable=algorithm, 
                        values=("Caesar", "Vigenere", "AES", "RSA"), 
                        state="readonly")
algo_box.grid(row=0, column=1, padx=5, pady=5)

algo_box.bind("<<ComboboxSelected>>", on_algo_change)

button_frame = tk.Frame(main_frame, bg="#eef2f5")
button_frame.grid(row=2, column=0, pady=10)

tk.Button(button_frame, text="Encrypt Message", command=encrypt, bg="#4CAF50", fg="white", width=15).grid(row=0, column=0, padx=10)
tk.Button(button_frame, text="Decrypt Message", command=decrypt, bg="#2196F3", fg="white", width=15).grid(row=0, column=1, padx=10)

output_frame = tk.LabelFrame(main_frame, text="Output", bg="#eef2f5", font=("Segoe UI", 10, "bold"), padx=10, pady=10)
output_frame.grid(row=3, column=0, sticky="nsew", pady=10)
output_frame.rowconfigure(0, weight=1)
output_frame.columnconfigure(0, weight=1)

output_text = tk.Text(output_frame, height=4, width=60, bg="white")
output_text.grid(row=0, column=0, sticky="nsew")

root.mainloop()