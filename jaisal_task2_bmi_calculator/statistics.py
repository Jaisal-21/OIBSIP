"""
statistics.py
------------------
Contains the Statistics Dashboard.
"""

import tkinter as tk
from tkinter import messagebox

from database import get_statistics


def show_statistics(root):
    """
    Displays BMI Statistics Dashboard.
    """

    stats = get_statistics()

    total_records = stats["total"]

    if total_records == 0:
        messagebox.showinfo(
            "No Data",
            "No BMI records available."
        )
        return

    # ---------------- Create Window ----------------

    stats_window = tk.Toplevel(root)

    stats_window.title("BMI Statistics")

    stats_window.geometry("420x360")

    stats_window.resizable(False, False)

    # ---------------- Title ----------------

    title = tk.Label(
        stats_window,
        text="BMI Statistics Dashboard",
        font=("Arial", 16, "bold")
    )

    title.pack(pady=15)

    # ---------------- Statistics Frame ----------------

    frame = tk.Frame(stats_window)

    frame.pack(pady=10)

    # ---------------- Statistics Labels ----------------

    labels = [

        ("Total Records", stats["total"]),

        ("Average BMI", f"{stats['average']:.2f}"),

        ("Highest BMI", f"{stats['maximum']:.2f}"),

        ("Lowest BMI", f"{stats['minimum']:.2f}"),

        ("Underweight Count", stats["underweight"]),

        ("Normal Weight Count", stats["normal"]),

        ("Overweight Count", stats["overweight"]),

        ("Obese Count", stats["obese"])

    ]

    for text, value in labels:

        row = tk.Frame(frame)

        row.pack(
            fill="x",
            padx=20,
            pady=5
        )

        tk.Label(
            row,
            text=text,
            font=("Arial", 11),
            width=20,
            anchor="w"
        ).pack(side="left")

        tk.Label(
            row,
            text=str(value),
            font=("Arial", 11, "bold"),
            fg="blue"
        ).pack(side="right")

    # ---------------- Close Button ----------------

    close_btn = tk.Button(
        stats_window,
        text="Close",
        width=12,
        command=stats_window.destroy
    )

    close_btn.pack(pady=20)