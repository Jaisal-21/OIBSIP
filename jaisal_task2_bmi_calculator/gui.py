"""
gui.py
-----------------------
Main GUI of the BMI Calculator.
"""

import tkinter as tk

from bmi import calculate_bmi
from bmi import bmi_category
from bmi import bmi_color

from database import save_record
from database import close_database

from history import view_history
from graph import show_bmi_graph
from statistics import show_statistics

from utils import (
    clear_fields,
    on_closing,
    validate_input,
    show_success,
    show_error
)


# ===================================================
# Create GUI
# ===================================================

def create_gui():

    root = tk.Tk()

    root.title("BMI Calculator")

    root.geometry("650x500")

    root.resizable(True, True)

    # ------------------------------------------------

    title_label = tk.Label(
        root,
        text="BMI Calculator",
        font=("Arial",20,"bold")
    )

    title_label.pack(pady=20)

    # ------------------------------------------------

    name_label = tk.Label(
        root,
        text="Name",
        font=("Arial",12)
    )

    name_label.pack()

    name_entry = tk.Entry(
        root,
        width=30
    )

    name_entry.pack(pady=5)

    # ------------------------------------------------

    weight_label = tk.Label(
        root,
        text="Weight (kg)",
        font=("Arial",12)
    )

    weight_label.pack()

    weight_entry = tk.Entry(
        root,
        width=30
    )

    weight_entry.pack(pady=5)

    # ------------------------------------------------

    height_label = tk.Label(
        root,
        text="Height (m)",
        font=("Arial",12)
    )

    height_label.pack()

    height_entry = tk.Entry(
        root,
        width=30
    )

    height_entry.pack(pady=5)

    # ------------------------------------------------

    result_label = tk.Label(
        root,
        text="",
        font=("Arial",14,"bold")
    )

    result_label.pack(pady=20)


        # ===================================================
    # Calculate BMI
    # ===================================================

    def calculate():

        name = name_entry.get().strip()

        weight = weight_entry.get()

        height = height_entry.get()

        valid, message = validate_input(
            name,
            weight,
            height
        )

        if not valid:

            show_error(message)

            return

        weight = float(weight)

        height = float(height)

        bmi = calculate_bmi(
            weight,
            height
        )

        category = bmi_category(bmi)

        color = bmi_color(category)

        save_record(
            name,
            weight,
            height,
            bmi,
            category
        )

        result_label.config(

            text=f"Name : {name}\n"
                 f"BMI : {bmi}\n"
                 f"Category : {category}",

            fg=color

        )

        show_success(
            "BMI Record Saved Successfully!"
        )

        # Clear only input fields
        name_entry.delete(0, tk.END)
        weight_entry.delete(0, tk.END)
        height_entry.delete(0, tk.END)

        name_entry.focus()


        # ===================================================
    # Button Frame
    # ===================================================

    button_frame = tk.Frame(root)

    button_frame.pack(pady=20)

    # ---------------- First Row ----------------

    calculate_btn = tk.Button(
        button_frame,
        text="Calculate BMI",
        font=("Arial",11,"bold"),
        width=15,
        command=calculate
    )

    calculate_btn.grid(
        row=0,
        column=0,
        padx=10,
        pady=8
    )

    clear_btn = tk.Button(
        button_frame,
        text="Clear",
        font=("Arial",11),
        width=15,
        command=lambda: clear_fields(
            name_entry,
            weight_entry,
            height_entry,
            result_label
        )
    )

    clear_btn.grid(
        row=0,
        column=1,
        padx=10,
        pady=8
    )

    exit_btn = tk.Button(
        button_frame,
        text="Exit",
        font=("Arial",11),
        width=15,
        bg="red",
        fg="white",
        command=lambda: on_closing(
            root,
            close_database
        )
    )

    exit_btn.grid(
        row=0,
        column=2,
        padx=10,
        pady=8
    )

    # ---------------- Second Row ----------------

    history_btn = tk.Button(
        button_frame,
        text="History",
        font=("Arial",11),
        width=15,
        command=lambda: view_history(root)
    )

    history_btn.grid(
        row=1,
        column=0,
        padx=10,
        pady=8
    )

    graph_btn = tk.Button(
        button_frame,
        text="Graph",
        font=("Arial",11),
        width=15,
        command=lambda: show_bmi_graph(
            name_entry.get().strip()
        )
    )

    graph_btn.grid(
        row=1,
        column=1,
        padx=10,
        pady=8
    )

    stats_btn = tk.Button(
        button_frame,
        text="Statistics",
        font=("Arial",11),
        width=15,
        command=lambda: show_statistics(root)
    )

    stats_btn.grid(
        row=1,
        column=2,
        padx=10,
        pady=8
    )

    # ===================================================
    # Window Close Button (X)
    # ===================================================

    root.protocol(
        "WM_DELETE_WINDOW",
        lambda: on_closing(
            root,
            close_database
        )
    )

    # ===================================================
    # Start GUI
    # ===================================================

    root.mainloop()