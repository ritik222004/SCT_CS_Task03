import re
import tkinter as tk
from tkinter import messagebox

def check_password_strength():
    password = entry.get()
    strength = 0
    feedback = []

    # Password Strength Rules
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("❌ At least 8 characters required.")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("❌ Include at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("❌ Include at least one lowercase letter.")

    if re.search(r"\d", password):
        strength += 1
    else:
        feedback.append("❌ Include at least one number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("❌ Include at least one special character.")

    # Result Message
    if strength == 5:
        result_label.config(text="✅ Strong Password!", fg="green")
    elif strength >= 3:
        result_label.config(text="⚠️ Medium Password!", fg="orange")
    else:
        result_label.config(text="❌ Weak Password!", fg="red")

    # Show feedback
    if feedback:
        messagebox.showinfo("Suggestions", "\n".join(feedback))

# GUI Setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x250")

# Widgets
tk.Label(root, text="Enter Password:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, width=30, show="*", font=("Arial", 12))
entry.pack()

btn = tk.Button(root, text="Check Strength", command=check_password_strength, font=("Arial", 12))
btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack()

root.mainloop()
