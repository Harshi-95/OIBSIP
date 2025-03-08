import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length, use_letters, use_digits, use_symbols):
    all_characters = ""
    if use_letters:
        all_characters += string.ascii_letters
    if use_digits:
        all_characters += string.digits
    if use_symbols:
        all_characters += string.punctuation

    if not all_characters:
        messagebox.showerror("Error", "At least one character type should be selected.")
        return

    password = []
    if use_letters:
        password.append(random.choice(string.ascii_letters))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_symbols:
        password.append(random.choice(string.punctuation))

    for _ in range(length - len(password)):
        password.append(random.choice(all_characters))

    random.shuffle(password)
    return "".join(password)

def check_password_strength(password):
    length = len(password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)

    if (length >= 12 and has_digit and has_special):
        return "Strong"
    elif length >= 8 and (has_digit or has_special):
        return "Medium"
    else:
        return "Weak"

def generate_and_display_password():
    try:
        length = int(entry_length.get())
        if length < 4:
            messagebox.showerror("Error", "Password length must be at least 4 characters.")
            return

        use_letters = letters_var.get()
        use_digits = digits_var.get()
        use_symbols = symbols_var.get()

        password = generate_password(length, use_letters, use_digits, use_symbols)
        if password:
            password_strength = check_password_strength(password)
            result_window = tk.Toplevel(root)
            result_window.title("Generated Password")
            result_window.geometry("300x250") 
            result_window.configure(bg="#f0f0f0")

            tk.Label(result_window, text="Generated Password:", font=("Arial", 18), bg="#f0f0f0", fg="#007bff").pack()
            tk.Label(result_window, text=password, font=("Monospace", 22), bg="#f0f0f0", fg="#28a745").pack()
            tk.Label(result_window, text=f"Password Strength: {password_strength}", font=("Arial", 18), bg="#f0f0f0", fg="#dc3545" if password_strength == "Weak" else "#28a745").pack()
            tk.Button(result_window, text="Close", command=result_window.destroy, font=("Arial", 14), bg="#007bff", fg="#ffffff").pack() 
    except ValueError:
        messagebox.showerror("Error", "Invalid password length.")

root = tk.Tk()
root.title("Password Generator")

tk.Label(root, text="Password Length:", font=("Arial", 16)).pack()
entry_length = tk.Entry(root, font=("Arial", 16))
entry_length.pack()

letters_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

tk.Checkbutton(root, text="Include Letters", variable=letters_var, font=("Arial", 16)).pack()
tk.Checkbutton(root, text="Include Digits", variable=digits_var, font=("Arial", 16)).pack()
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var, font=("Arial", 16)).pack()

tk.Button(root, text="Generate Password", command=generate_and_display_password, font=("Arial", 14), bg="#007bff", fg="#ffffff").pack() # Decreased button font size

root.mainloop()