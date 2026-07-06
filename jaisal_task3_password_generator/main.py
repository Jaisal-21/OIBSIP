import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pyperclip
from datetime import datetime

from utils.generator import generate_password
from utils.strength import check_password_strength


# ----------------------------
# Main Window
# ----------------------------
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("1000x950")
root.minsize(1000, 950)
root.resizable(True, True)
root.configure(bg="#1e1e2f")


# ----------------------------
# Styles
# ----------------------------
style = ttk.Style()

style.theme_use("clam")

style.configure(
    "TLabel",
    background="#1e1e2f",
    foreground="white",
    font=("Segoe UI", 11)
)

style.configure(
    "TCheckbutton",
    background="#1e1e2f",
    foreground="white",
    font=("Segoe UI", 11)
)

style.configure(
    "TButton",
    font=("Segoe UI", 11, "bold"),
    padding=8
)

# -----------------------------
# Treeview Style
# -----------------------------

style.configure(
    "Treeview",
    background="#2d2d44",
    foreground="white",
    fieldbackground="#2d2d44",
    rowheight=28,
    font=("Consolas", 10),
    borderwidth=0
)

style.configure(
    "Treeview.Heading",
    background="#3b3b5c",
    foreground="white",
    font=("Segoe UI", 10, "bold")
)

style.map(
    "Treeview",
    background=[("selected", "#4CAF50")],
    foreground=[("selected", "white")]
)


# ----------------------------
# Generate Password Function
# ----------------------------
def generate_password_gui():

    password = generate_password(
        length=length_var.get(),
        use_upper=upper_var.get(),
        use_lower=lower_var.get(),
        use_digits=digits_var.get(),
        use_symbols=symbols_var.get()
    )

    if password is None:
        messagebox.showerror(
            "Selection Error",
            "Please select at least one character type."
        )

        update_status(
        "❌ No character type selected.",
        "red"
        )

        return

    password_entry.config(state="normal")
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    password_entry.config(state="readonly")
    strength, color = check_password_strength(password)

    strength_label.config(
    text=f"Strength: {strength}",
    fg=color
    )
    add_to_history(password)
    update_status(
    "✔ Password generated successfully.",
    "lightgreen"
    )

# ----------------------------
# Title
# ----------------------------
title = tk.Label(
    root,
    text="Random Password Generator",
    font=("Segoe UI", 22, "bold"),
    bg="#1e1e2f",
    fg="white"
)

title.pack(pady=20)


# ============================
# Password Display
# ============================

password_label = ttk.Label(
    root,
    text="Generated Password:"
)
password_label.pack(anchor="w", padx=50)

password_entry = ttk.Entry(
    root,
    width=55,
    font=("Consolas", 14),
    state="readonly"
)
password_entry.pack(pady=10)


# ============================
# Password Length
# ============================

length_label = ttk.Label(
    root,
    text="Password Length:"
)
length_label.pack(anchor="w", padx=50, pady=(20, 5))

length_var = tk.IntVar(value=12)

length_spinbox = ttk.Spinbox(
    root,
    from_=4,
    to=64,
    textvariable=length_var,
    width=10
)
length_spinbox.pack(anchor="w", padx=50)


# ============================
# Checkboxes
# ============================

upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

ttk.Checkbutton(
    root,
    text="Include Uppercase Letters",
    variable=upper_var
).pack(anchor="w", padx=50, pady=5)

ttk.Checkbutton(
    root,
    text="Include Lowercase Letters",
    variable=lower_var
).pack(anchor="w", padx=50, pady=5)

ttk.Checkbutton(
    root,
    text="Include Numbers",
    variable=digits_var
).pack(anchor="w", padx=50, pady=5)

ttk.Checkbutton(
    root,
    text="Include Symbols",
    variable=symbols_var
).pack(anchor="w", padx=50, pady=5)


# ----------------------------
# Copy Password
# ----------------------------
def copy_password():

    password = password_entry.get()

    if password == "":
        messagebox.showwarning(
            "No Password",
            "Generate a password first."
        )
        return

    pyperclip.copy(password)

    update_status(
    "✔ Password copied to clipboard.",
    "cyan"
    )

# ----------------------------
# Clear Fields
# ----------------------------
def clear_fields():

    password_entry.config(state="normal")
    password_entry.delete(0, tk.END)
    password_entry.config(state="readonly")

    strength_label.config(
        text="Strength: -",
        fg="white"
    )

    update_status(
        "✔ Fields cleared.",
        "orange"
    )

# ----------------------------
# Update Status Bar
# ----------------------------
def update_status(message, color="white"):
    status_label.config(
        text=message,
        fg=color
    )

# ----------------------------
# Save Password to History
# ----------------------------
from datetime import datetime

def save_to_history(password):

    now = datetime.now()

    date = now.strftime("%d-%m-%Y")
    time = now.strftime("%I:%M:%S %p")

    with open("data/history.txt", "a") as file:
        file.write(f"{date}|{time}|{password}\n")


# ----------------------------
# Load Password History
# ----------------------------
def load_history():

    history_tree.delete(*history_tree.get_children())

    try:
        with open("data/history.txt", "r") as file:

            lines = file.readlines()

            for i, line in enumerate(reversed(lines)):

                data = line.strip().split("|")

                if len(data) == 3:

                    tag = "even" if i % 2 == 0 else "odd"

                    history_tree.insert(
                    "",
                    "end",
                    values=(data[0], data[1], data[2]),
                    tags=(tag,)
                    )

    except FileNotFoundError:
        pass


# ----------------------------
# Add Password to History
# ----------------------------
def add_to_history(password):

    now = datetime.now()

    date = now.strftime("%d-%m-%Y")
    time = now.strftime("%I:%M:%S %p")

    save_to_history(password)

    row_count = len(history_tree.get_children())

    tag = "even" if row_count % 2 == 0 else "odd"

    history_tree.insert(
    "",
    0,
    values=(date, time, password),
    tags=(tag,)
    )

# ============================
# Buttons
# ============================

button_frame = tk.Frame(
    root,
    bg="#1e1e2f"
)

button_frame.pack(pady=30)



# ============================
# Password History
# ============================

history_title = tk.Label(
    root,
    text="Password History",
    bg="#1e1e2f",
    fg="white",
    font=("Segoe UI", 13, "bold")
)
history_title.pack(pady=(20, 8))

history_frame = tk.Frame(root, bg="#1e1e2f")
history_frame.pack(pady=5)

columns = ("Date", "Time", "Password")

history_tree = ttk.Treeview(
    history_frame,
    columns=columns,
    show="headings",
    height=8
)

history_tree.heading("Date", text="Date")
history_tree.heading("Time", text="Time")
history_tree.heading("Password", text="Password")

history_tree.column("Date", width=120, anchor="center")
history_tree.column("Time", width=120, anchor="center")
history_tree.column("Password", width=450, anchor="center")

scrollbar = ttk.Scrollbar(
    history_frame,
    orient="vertical",
    command=history_tree.yview
)

history_tree.configure(yscrollcommand=scrollbar.set)

history_tree.grid(row=0, column=0)
scrollbar.grid(row=0, column=1, sticky="ns")


history_tree.tag_configure(
    "even",
    background="#2d2d44",
    foreground="white"
)

history_tree.tag_configure(
    "odd",
    background="#25253a",
    foreground="white"
)





generate_btn = ttk.Button(
    button_frame,
    text="Generate Password",
    command=generate_password_gui
)

generate_btn.grid(
    row=0,
    column=0,
    padx=10
)


copy_btn = ttk.Button(
    button_frame,
    text="Copy Password",
    command=copy_password
)

copy_btn.grid(
    row=0,
    column=1,
    padx=10
)


clear_btn = ttk.Button(
    button_frame,
    text="Clear",
    command=clear_fields
)

clear_btn.grid(
    row=0,
    column=2,
    padx=10
)


# ============================
# Password Strength
# ============================

strength_label = tk.Label(
    root,
    text="Strength: -",
    font=("Segoe UI", 12, "bold"),
    bg="#1e1e2f",
    fg="white"
)

strength_label.pack(pady=15)


# ============================
# Status Bar
# ============================

status_label = tk.Label(
    root,
    text="Ready",
    anchor="w",
    bg="#2d2d44",
    fg="white",
    font=("Segoe UI", 10)
)

status_label.pack(side="bottom", fill="x")




load_history()

# ----------------------------
# Run
# ----------------------------
root.mainloop()