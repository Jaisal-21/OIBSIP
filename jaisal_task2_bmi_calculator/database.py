"""
database.py
------------
Handles all SQLite database operations.
"""

import sqlite3
from datetime import datetime

# ---------------------------------------------------
# Database Connection
# ---------------------------------------------------

conn = sqlite3.connect("database.db")

cursor = conn.cursor()

# ---------------------------------------------------
# Create Table
# ---------------------------------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS bmi_records(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT,

    weight REAL,

    height REAL,

    bmi REAL,

    category TEXT,

    date TEXT,

    time TEXT

)
""")

conn.commit()

# ---------------------------------------------------
# Save Record
# ---------------------------------------------------

def save_record(name, weight, height, bmi, category):

    current_date = datetime.now().strftime("%d-%m-%Y")
    current_time = datetime.now().strftime("%H:%M:%S")

    cursor.execute("""

    INSERT INTO bmi_records
    (name, weight, height, bmi, category, date, time)

    VALUES (?, ?, ?, ?, ?, ?, ?)

    """, (

        name,
        weight,
        height,
        bmi,
        category,
        current_date,
        current_time

    ))

    conn.commit()


# ---------------------------------------------------
# Load All Records
# ---------------------------------------------------

def get_all_records():

    cursor.execute("""

    SELECT *

    FROM bmi_records

    ORDER BY id

    """)

    return cursor.fetchall()


# ---------------------------------------------------
# Search Record
# ---------------------------------------------------

def search_records(name):

    cursor.execute("""

    SELECT *

    FROM bmi_records

    WHERE LOWER(name) LIKE LOWER(?)

    ORDER BY id

    """, (f"%{name}%",))

    return cursor.fetchall()


# ---------------------------------------------------
# Get Graph Data
# ---------------------------------------------------

def get_graph_data(name):

    cursor.execute("""

    SELECT
        date,
        bmi

    FROM bmi_records

    WHERE LOWER(name)=LOWER(?)

    ORDER BY id

    """, (name,))

    return cursor.fetchall()


# ---------------------------------------------------
# Statistics
# ---------------------------------------------------

def get_statistics():

    stats = {}

    # Total Records
    cursor.execute("""
    SELECT COUNT(*)
    FROM bmi_records
    """)
    stats["total"] = cursor.fetchone()[0]

    if stats["total"] == 0:
        return stats

    # Average BMI
    cursor.execute("""
    SELECT AVG(bmi)
    FROM bmi_records
    """)
    stats["average"] = cursor.fetchone()[0]

    # Maximum BMI
    cursor.execute("""
    SELECT MAX(bmi)
    FROM bmi_records
    """)
    stats["maximum"] = cursor.fetchone()[0]

    # Minimum BMI
    cursor.execute("""
    SELECT MIN(bmi)
    FROM bmi_records
    """)
    stats["minimum"] = cursor.fetchone()[0]

    # Underweight
    cursor.execute("""
    SELECT COUNT(*)
    FROM bmi_records
    WHERE category='Underweight'
    """)
    stats["underweight"] = cursor.fetchone()[0]

    # Normal
    cursor.execute("""
    SELECT COUNT(*)
    FROM bmi_records
    WHERE category='Normal Weight'
    """)
    stats["normal"] = cursor.fetchone()[0]

    # Overweight
    cursor.execute("""
    SELECT COUNT(*)
    FROM bmi_records
    WHERE category='Overweight'
    """)
    stats["overweight"] = cursor.fetchone()[0]

    # Obese
    cursor.execute("""
    SELECT COUNT(*)
    FROM bmi_records
    WHERE category='Obese'
    """)
    stats["obese"] = cursor.fetchone()[0]

    return stats


# ---------------------------------------------------
# Delete Record (Future Feature)
# ---------------------------------------------------

def delete_record(record_id):

    cursor.execute("""

    DELETE FROM bmi_records

    WHERE id=?

    """, (record_id,))

    conn.commit()


# ---------------------------------------------------
# Close Database
# ---------------------------------------------------

def close_database():

    conn.close()