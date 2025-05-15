import tkinter as tk
from tkinter import messagebox


def encrypt_caesar(text, key):
    encrypted = ""
    for char in text:
        if char.isalpha():
            shift = key % 26
            base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        elif char.isdigit():
            encrypted += str((int(char) + key) % 10)
        else:
            encrypted += char
    return encrypted


def decrypt_caesar(text, key):
    decrypted = ""
    for char in text:
        if char.isalpha():
            shift = key % 26
            base = ord('A') if char.isupper() else ord('a')
            decrypted += chr((ord(char) - base - shift) % 26 + base)
        elif char.isdigit():
            decrypted += str((int(char) - key + 10) % 10)
        else:
            decrypted += char
    return decrypted


def perform_encryption():
    try:
        message = entry_message.get()
        key = int(entry_key.get())
        result = encrypt_caesar(message, key)
        output_var.set(f"Encrypted: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer for the key.")

def perform_decryption():
    try:
        message = entry_message.get()
        key = int(entry_key.get())
        result = decrypt_caesar(message, key)
        output_var.set(f"Decrypted: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer for the key.")

root = tk.Tk()
root.title("Caesar Cipher Tool")
root.geometry("400x250")
root.resizable(False, False)

tk.Label(root, text="Enter Message:").pack(pady=5)
entry_message = tk.Entry(root, width=50)
entry_message.pack()

tk.Label(root, text="Enter Shift Key:").pack(pady=5)
entry_key = tk.Entry(root, width=10)
entry_key.pack()

tk.Button(root, text="Encrypt", command=perform_encryption, width=15).pack(pady=10)
tk.Button(root, text="Decrypt", command=perform_decryption, width=15).pack()

output_var = tk.StringVar()
tk.Label(root, textvariable=output_var, fg="blue", wraplength=380).pack(pady=15)

root.mainloop()
