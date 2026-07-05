"""
graph.py
---------
Contains all graph-related functions.
"""

import matplotlib.pyplot as plt
from tkinter import messagebox

from database import get_graph_data


def show_bmi_graph(name):
    """
    Displays BMI Trend Graph for a particular user.
    """

    # ---------------- Validation ----------------

    if name.strip() == "":
        messagebox.showerror(
            "Error",
            "Please enter a name."
        )
        return

    # ---------------- Fetch Data ----------------

    records = get_graph_data(name)

    if len(records) == 0:

        messagebox.showinfo(
            "No Data",
            f"No records found for '{name}'."
        )

        return

    # ---------------- Separate Date & BMI ----------------

    dates = []
    bmi_values = []

    for row in records:

        dates.append(row[0])
        bmi_values.append(row[1])

    # ---------------- Create Figure ----------------

    plt.figure(figsize=(9,5))

    plt.plot(
        dates,
        bmi_values,
        marker="o",
        linewidth=2,
        color="blue",
        label="BMI"
    )

    # ---------------- BMI Reference Lines ----------------

    plt.axhline(
        y=18.5,
        color="green",
        linestyle="--",
        linewidth=1,
        label="Underweight (18.5)"
    )

    plt.axhline(
        y=25,
        color="orange",
        linestyle="--",
        linewidth=1,
        label="Overweight (25)"
    )

    plt.axhline(
        y=30,
        color="red",
        linestyle="--",
        linewidth=1,
        label="Obesity (30)"
    )

    # ---------------- Labels ----------------

    plt.title(f"{name}'s BMI Trend")

    plt.xlabel("Date")

    plt.ylabel("BMI")

    plt.xticks(rotation=45)

    plt.grid(True)

    plt.legend()

    plt.tight_layout()

    plt.show()