import tkinter as tk
from tkinter import messagebox
from zxcvbn import zxcvbn

def analyze_password():
    password = entry.get()
    if not password:
        messagebox.showwarning("⚠️ Oops!", "Please enter a password")
        return

    result = zxcvbn(password)
    score = result['score']
    crack_times = result['crack_times_display']

    score_label.config(text=f"🔒 Strength Score: {score}/4", fg=score_colors[score])

    result_box.config(state='normal')
    result_box.delete('1.0', tk.END)
    result_box.insert(tk.END, "Estimated Crack Times:\n\n")
    for k, v in crack_times.items():
        label = k.replace('_', ' ').capitalize()
        result_box.insert(tk.END, f"{label}: {v}\n")
    result_box.config(state='disabled')

# --- UI Setup ---
root = tk.Tk()
root.title("✨ Password Strength Analyzer")
root.geometry("600x500")
root.resizable(False, False)
root.config(bg="#1b1b1b")

# Colors & Style
bg_color = "#1b1b1b"
fg_color = "#ffffff"
accent = "#e1306c"  # Instagram pink
btn_color = "#833ab4"  # Gradient purple
entry_bg = "#2c2c2c"
score_colors = ['#ff4d4d', '#ff944d', '#ffcc00', '#66cc66', '#00cc99']

# Header
header = tk.Label(root, text="🔐 Password Strength Analyzer", font=('Segoe UI', 18, 'bold'), bg=bg_color, fg=accent)
header.pack(pady=20)

# Entry Field
entry_label = tk.Label(root, text="Enter Password Below:", font=('Segoe UI', 12), bg=bg_color, fg=fg_color)
entry_label.pack()

entry = tk.Entry(root, width=35, show="*", font=('Segoe UI', 13), bg=entry_bg, fg=fg_color, insertbackground='white', relief=tk.FLAT)
entry.pack(pady=10, ipady=6)

# Analyze Button
analyze_btn = tk.Button(
    root, text="Analyze Password", font=('Segoe UI', 12, 'bold'),
    bg=btn_color, fg='white', activebackground=accent,
    relief=tk.FLAT, padx=20, pady=5, command=analyze_password
)
analyze_btn.pack(pady=15)

# Score Label
score_label = tk.Label(root, text="", font=('Segoe UI', 13, 'bold'), bg=bg_color, fg=fg_color)
score_label.pack()

# Results Text Box
result_box = tk.Text(root, height=10, width=60, bg="#1e1e1e", fg=fg_color, font=('Courier New', 10), relief=tk.FLAT)
result_box.pack(pady=10)
result_box.config(state='disabled')

# Footer
footer = tk.Label(root, text="Made with ❤️ for Cybersecurity Portfolio", font=('Segoe UI', 9), bg=bg_color, fg="#aaaaaa")
footer.pack(pady=15)

root.mainloop()
