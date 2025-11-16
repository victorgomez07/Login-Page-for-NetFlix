import tkinter as tk
from tkinter import messagebox

APP_BG = "#465247"     # dark slate green
ACCENT = "#FFCC00"     # gold accent
ENTRY_BG = "#D6FFD6"   # mint green
SCREEN_W = 400
SCREEN_H = 750


# ------------------------------------------------
# Helper: Clear window
# ------------------------------------------------
def clear_window(win):
    for widget in win.winfo_children():
        widget.destroy()


# ------------------------------------------------
# Change Password Page (same window)
# ------------------------------------------------
def change_password_page(root):
    clear_window(root)
    root.configure(bg=APP_BG)

    tk.Label(root, text="Account",
             font=("Arial", 26, "bold"),
             fg=ACCENT, bg=APP_BG).pack(pady=10)

    tk.Frame(root, bg=ACCENT, height=3).pack(fill="x", padx=20)

    tk.Label(root, text="Change Password",
             font=("Arial", 28, "bold"),
             fg=ACCENT, bg=APP_BG).pack(pady=30)

    # ----- Fields -----
    def add_field(label):
        tk.Label(root, text=label,
                 font=("Arial", 16, "bold"),
                 fg=ACCENT, bg=APP_BG).pack(anchor="w", padx=30)
        entry = tk.Entry(root, bg=ENTRY_BG, font=("Arial", 16), bd=0)
        entry.pack(pady=10, ipadx=50, ipady=10, padx=30)
        return entry

    email = add_field("Email")
    verify_email = add_field("Verify Email")
    new_pass = add_field("New Password")
    verify_pass = add_field("Verify New Password")

    # Submit button
    def submit():
        if email.get() != verify_email.get():
            messagebox.showerror("Error", "Emails do not match.")
            return
        if new_pass.get() != verify_pass.get():
            messagebox.showerror("Error", "Passwords do not match.")
            return

        messagebox.showinfo("Success", "Password updated successfully!")

    tk.Button(root, text="Submit",
              bg=ACCENT, fg="black",
              font=("Arial", 18, "bold"),
              bd=0, padx=50, pady=12,
              command=submit).pack(pady=40)


# ------------------------------------------------
# Login Page (main → leads to Change Password)
# ------------------------------------------------
def login_page(root):
    clear_window(root)
    root.configure(bg=APP_BG)

    tk.Label(root, text="Login",
             font=("Arial", 28, "bold"),
             fg=ACCENT, bg=APP_BG).pack(pady=40)

    # Email
    email_entry = tk.Entry(root, bg=ENTRY_BG, font=("Arial", 16), bd=0)
    email_entry.pack(pady=10, ipadx=50, ipady=10)

    # Password
    password_entry = tk.Entry(root, bg=ENTRY_BG, font=("Arial", 16), bd=0, show="*")
    password_entry.pack(pady=10, ipadx=50, ipady=10)

    # Login Button
    tk.Button(root, text="Login",
              bg=ACCENT, fg="black",
              font=("Arial", 16, "bold"),
              bd=0, padx=40, pady=10).pack(pady=20)

    # Forgot Password Link → SAME WINDOW
    tk.Button(root, text="Forgot Password?",
              bg=APP_BG, fg=ACCENT,
              font=("Arial", 14, "underline"),
              bd=0,
              command=lambda: change_password_page(root)).pack(pady=10)


# ------------------------------------------------
# Start App
# ------------------------------------------------
root = tk.Tk()
root.title("Movie App")
root.geometry(f"{SCREEN_W}x{SCREEN_H}")
root.resizable(False, False)
login_page(root)
root.mainloop()
