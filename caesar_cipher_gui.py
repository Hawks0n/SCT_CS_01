import tkinter as tk
from tkinter import messagebox

#Function for Caesar Cipher logic
def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            if mode == "encrypt":
                result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
            elif mode == "decrypt":
                result += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            result += char
    return result

# Encrypt button click handler
def encrypt_text():
    message = entry_message.get("1.0", tk.END).strip()
    shift_value = shift_entry.get()
    
    if not shift_value.isdigit():
        messagebox.showerror("Invalid Input", "Shift value must be a number!")
        return
    
    shift = int(shift_value)
    encrypted = caesar_cipher(message, shift, "encrypt")
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, encrypted)

# Decrypt button click handler
def decrypt_text():
    message = entry_message.get("1.0", tk.END).strip()
    shift_value = shift_entry.get()
    
    if not shift_value.isdigit():
        messagebox.showerror("Invalid Input", "Shift value must be a number!")
        return
    
    shift = int(shift_value)
    decrypted = caesar_cipher(message, shift, "decrypt")
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, decrypted)

# Create the main window
root = tk.Tk()
root.title("Caesar Cipher Encryptor/Decryptor")
root.geometry("500x400")
root.resizable(False, False)

# UI Elements
tk.Label(root, text="Enter your message:", font=("Helvetica", 12)).pack(pady=5)
entry_message = tk.Text(root, height=5, width=55)
entry_message.pack(pady=5)

tk.Label(root, text="Shift value (0-25):", font=("Helvetica", 12)).pack(pady=5)
shift_entry = tk.Entry(root, width=10, font=("Helvetica", 12))
shift_entry.pack(pady=5)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

encrypt_btn = tk.Button(btn_frame, text="Encrypt", command=encrypt_text, width=15, bg="#4CAF50", fg="white", font=("Helvetica", 10))
encrypt_btn.grid(row=0, column=0, padx=10)

decrypt_btn = tk.Button(btn_frame, text="Decrypt", command=decrypt_text, width=15, bg="#2196F3", fg="white", font=("Helvetica", 10))
decrypt_btn.grid(row=0, column=1, padx=10)

tk.Label(root, text="Output:", font=("Helvetica", 12)).pack(pady=5)
output_text = tk.Text(root, height=5, width=55, fg="black")
output_text.pack(pady=5)

tk.Label(root, text="Developed by Alpha01 🦅", font=("Helvetica", 9, "italic"), fg="gray").pack(side="bottom", pady=5)

# Run the GUI
root.mainloop()
