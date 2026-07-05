"""
utils.py
---------
Contains reusable utility functions for the BMI Calculator.
"""

import tkinter as tk
from tkinter import messagebox


# -------------------------------------------------
# Clear Input Fields
# -------------------------------------------------

def clear_fields(name_entry, weight_entry, height_entry, result_label):
    """
    Clear all input fields and reset the result label.
    """

    name_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)

    result_label.config(
        text="",
        fg="black"
    )

    name_entry.focus()


# -------------------------------------------------
# Exit Application
# -------------------------------------------------

def on_closing(root, close_database):
    """
    Ask confirmation before exiting the application.
    """

    answer = messagebox.askyesno(
        "Exit",
        "Are you sure you want to exit?"
    )

    if answer:
        close_database()
        root.destroy()


# -------------------------------------------------
# Show Success Message
# -------------------------------------------------

def show_success(message):

    messagebox.showinfo(
        "Success",
        message
    )


# -------------------------------------------------
# Show Error Message
# -------------------------------------------------

def show_error(message):

    messagebox.showerror(
        "Error",
        message
    )


# -------------------------------------------------
# Show Warning Message
# -------------------------------------------------

def show_warning(message):

    messagebox.showwarning(
        "Warning",
        message
    )


# -------------------------------------------------
# Validate User Input
# -------------------------------------------------

def validate_input(name, weight, height):
    """
    Validates user input.

    Returns:
        (True, "") if valid
        (False, error_message) if invalid
    """

    if name == "":
        return False, "Please enter your name."

    try:
        weight = float(weight)
        height = float(height)

    except ValueError:
        return False, "Weight and Height must be numbers."

    if weight <= 0:
        return False, "Weight must be greater than zero."

    if height <= 0:
        return False, "Height must be greater than zero."

    if weight > 500:
        return False, "Please enter a valid weight."

    if height > 3:
        return False, "Please enter height in meters."

    return True, ""


# -------------------------------------------------
# Center Any Window
# -------------------------------------------------

def center_window(window, width, height):
    """
    Centers a Tkinter window on the screen.
    """

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    window.geometry(f"{width}x{height}+{x}+{y}")