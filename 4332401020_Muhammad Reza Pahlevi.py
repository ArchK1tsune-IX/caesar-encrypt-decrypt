# Import Library Tkinter
from tkinter import messagebox
import tkinter as tk

# Function Caesar Encrypt
def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

# Function Caesar Decrypt
def caesar_decrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result

# Function Validate Shift
def validate_shift():
    try:
        shift = int(shift_var.get())
        if shift < 1 or shift > 25:
            raise ValueError
        return shift
    except ValueError:
        messagebox.showwarning("Invalid Input", "Shift must be a number between 1 and 25. Defaulting to 1.")
        return 1

# Function Process Caesar
def process_cipher():
    text = input_text.get("1.0", "end-1c")
    shift = validate_shift()
    mode = mode_var.get()

    if mode == "Encrypt":
        result = caesar_encrypt(text, shift)
    else:
        result = caesar_decrypt(text, shift)

    result_text.delete("1.0", "end")
    result_text.insert("1.0", result)

# Aplication GUI Setup
root = tk.Tk()
root.title("Caesar Cipher Tools")
root.geometry("700x400")
root.configure(bg="#95e0ff")

# Label judul aplikasi
title_label = tk.Label(root, text="Welcome to Caesar Encrypt/Decrypt Tools", font=("Poppins", 16, "bold"), bg="#95e0ff")
title_label.pack(pady=(15, 10))

# Konfigurasi main frame
main_frame = tk.Frame(root, bg="#95e0ff")
main_frame.pack(padx=10, pady=(10, 20))

# Membuat input text area
input_label = tk.Label(main_frame, text="Input text", font=("Poppins", 12, "bold"), bg="#95e0ff")
input_label.grid(row=0, column=0, padx=10, pady=5)

input_text = tk.Text(main_frame, width=30, height=10, font=("Poppins", 10), bg="#ffffff", relief="solid")
input_text.grid(row=1, column=0, padx=10, pady=5)

# Membuat shift + radio button frame
options_frame = tk.Frame(main_frame, bg="#95e0ff")
options_frame.grid(row=1, column=1, padx=10, pady=5)

# Shift Selector
shift_label = tk.Label(options_frame, text="Shift", font=("Helvetica", 12, "bold"), bg="#95e0ff")
shift_label.grid(row=0, column=0, pady=5)

shift_var = tk.StringVar(value=1)
shift_spinbox = tk.Spinbox(options_frame, from_=1, to=25, textvariable=shift_var, width=5, font=("Helvetica", 10), relief="solid")
shift_spinbox.grid(row=1, column=0, pady=5)

# Radio Buttons
mode_var = tk.StringVar(value="Encrypt")

encrypt_radio = tk.Radiobutton(options_frame, text="Encrypt", variable=mode_var, value="Encrypt", font=("Helvetica", 10), bg="#95e0ff")
encrypt_radio.grid(row=2, column=0, pady=5, sticky="w")

decrypt_radio = tk.Radiobutton(options_frame, text="Decrypt", variable=mode_var, value="Decrypt", font=("Helvetica", 10), bg="#95e0ff")
decrypt_radio.grid(row=3, column=0, pady=5, sticky="w")

# Result Text Area
result_label = tk.Label(main_frame, text="Result", font=("Helvetica", 12, "bold"), bg="#95e0ff")
result_label.grid(row=0, column=2, padx=10, pady=5)

result_text = tk.Text(main_frame, width=30, height=10, font=("Helvetica", 10), bg="#ffffff", relief="solid")
result_text.grid(row=1, column=2, padx=10, pady=5)

# Submit Button
submit_button = tk.Button(root, text="Submit", command=process_cipher, font=("Helvetica", 12, "bold"), bg="#1E90FF", fg="#ffffff", relief="raised")
submit_button.pack(pady=10)

# Footer
footer_label = tk.Label(root, text="© 2024 Caesar Cipher Tool. All Rights Reserved.", font=("Helvetica", 8), bg="#95e0ff", fg="#808080")
footer_label.pack(side="bottom", pady=(20, 10))  # Padding atas lebih besar untuk jarak dengan frame

# Jalankan aplikasi
root.mainloop()
