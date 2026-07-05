import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from database import get_all_records
from database import search_records


def view_history(root):

    history_window = tk.Toplevel(root)
    history_window.title("BMI History")
    history_window.geometry("950x500")

    # ================= Search Frame =================

    search_frame = tk.Frame(history_window)
    search_frame.pack(pady=10)

    tk.Label(
        search_frame,
        text="Search Name:",
        font=("Arial", 11)
    ).pack(side="left", padx=5)

    search_entry = tk.Entry(
        search_frame,
        width=25,
        font=("Arial", 11)
    )

    search_entry.pack(side="left", padx=5)

    # ================= Table Frame =================

    frame = tk.Frame(history_window)
    frame.pack(fill="both", expand=True)

    # ================= Treeview =================

    columns = (
        "ID",
        "Name",
        "Weight",
        "Height",
        "BMI",
        "Category",
        "Date",
        "Time"
    )

    tree = ttk.Treeview(
        frame,
        columns=columns,
        show="headings"
    )

    # ================= Headings =================

    tree.heading("ID", text="ID")
    tree.heading("Name", text="Name")
    tree.heading("Weight", text="Weight (kg)")
    tree.heading("Height", text="Height (m)")
    tree.heading("BMI", text="BMI")
    tree.heading("Category", text="Category")
    tree.heading("Date", text="Date")
    tree.heading("Time", text="Time")

    # ================= Columns =================

    tree.column("ID", width=60, anchor="center")
    tree.column("Name", width=160, anchor="center")
    tree.column("Weight", width=100, anchor="center")
    tree.column("Height", width=100, anchor="center")
    tree.column("BMI", width=80, anchor="center")
    tree.column("Category", width=150, anchor="center")
    tree.column("Date", width=120, anchor="center")
    tree.column("Time", width=120, anchor="center")

    # ================= Scrollbars =================

    vertical_scroll = ttk.Scrollbar(
        frame,
        orient="vertical",
        command=tree.yview
    )

    horizontal_scroll = ttk.Scrollbar(
        frame,
        orient="horizontal",
        command=tree.xview
    )

    tree.configure(
        yscrollcommand=vertical_scroll.set,
        xscrollcommand=horizontal_scroll.set
    )

    tree.grid(row=0, column=0, sticky="nsew")
    vertical_scroll.grid(row=0, column=1, sticky="ns")
    horizontal_scroll.grid(row=1, column=0, sticky="ew")

    frame.rowconfigure(0, weight=1)
    frame.columnconfigure(0, weight=1)

    # ================= Zebra Rows =================

    tree.tag_configure(
        "even",
        background="#F2F2F2"
    )

    tree.tag_configure(
        "odd",
        background="white"
    )

    # ================= Load Data =================

    def load_table(records):

        # Clear previous rows
        for item in tree.get_children():
            tree.delete(item)

        # Insert rows
        for index, row in enumerate(records):

            tag = "even" if index % 2 == 0 else "odd"

            tree.insert(
                "",
                tk.END,
                values=row,
                tags=(tag,)
            )

    # ================= Search =================

    def search():

        name = search_entry.get().strip()

        if name == "":
            messagebox.showwarning(
                "Warning",
                "Please enter a name."
            )
            return

        records = search_records(name)

        load_table(records)

    # ================= Show All =================

    def show_all():

        search_entry.delete(0, tk.END)

        records = get_all_records()

        load_table(records)

    # ================= Buttons =================

    search_button = tk.Button(
        search_frame,
        text="Search",
        width=10,
        command=search
    )

    search_button.pack(
        side="left",
        padx=5
    )

    show_button = tk.Button(
        search_frame,
        text="Show All",
        width=10,
        command=show_all
    )

    show_button.pack(
        side="left",
        padx=5
    )

    # ================= Enter Key =================

    search_entry.bind(
        "<Return>",
        lambda event: search()
    )

    # ================= Initial Load =================

    show_all()