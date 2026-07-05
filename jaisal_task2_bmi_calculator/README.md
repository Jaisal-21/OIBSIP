# 🩺 BMI Calsculator

A professional **Body Mass Index (BMI) Calculator** developed using **Python, Tkinter, SQLite, and Matplotlib**. This desktop application allows users to calculate their BMI, store historical records, visualize BMI trends, and view statistical insights through a user-friendly graphical interface.

---

## 📌 Features

### ✅ BMI Calculation
- Calculate BMI using weight (kg) and height (m).
- Accurate BMI calculation using the standard BMI formula.
- Displays BMI up to two decimal places.

### ✅ BMI Classification
Automatically categorizes BMI into:
- Underweight
- Normal Weight
- Overweight
- Obese

### ✅ Color-Coded Results
BMI results are displayed with different colors:
- 🔵 Blue → Underweight
- 🟢 Green → Normal Weight
- 🟠 Orange → Overweight
- 🔴 Red → Obese

### ✅ SQLite Database
- Stores every BMI record permanently.
- Saves:
  - Name
  - Weight
  - Height
  - BMI
  - Category
  - Date
  - Time

### ✅ History Management
- View all previously saved records.
- Search records by user name.
- Scrollable history table.
- Alternate row colors for better readability.

### ✅ BMI Trend Graph
- Displays BMI progression for a selected user.
- Date-based graph.
- Includes BMI reference lines:
  - 18.5
  - 25
  - 30

### ✅ Statistics Dashboard
Displays:
- Total Records
- Average BMI
- Highest BMI
- Lowest BMI
- Underweight Count
- Normal Weight Count
- Overweight Count
- Obese Count

### ✅ Input Validation
- Prevents empty inputs.
- Prevents invalid numbers.
- Handles incorrect user input gracefully.

### ✅ Professional GUI
- Tkinter-based graphical interface
- Two-row button layout
- Clear Button
- Exit Confirmation
- Responsive windows

---

# 🛠️ Technologies Used

- Python 3.x
- Tkinter
- SQLite3
- Matplotlib
- Datetime

---

# 📂 Project Structure

```
BMI_Calculator/
│
├── main.py                 # Entry point
├── gui.py                  # Main GUI
├── bmi.py                  # BMI calculation logic
├── database.py             # Database operations
├── history.py              # History window
├── graph.py                # BMI graph
├── statistics.py           # Statistics dashboard
├── utils.py                # Utility functions
│
├── database.db             # SQLite database
├── requirements.txt
├── README.md

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/BMI_Calculator.git
```

Move into the project folder

```bash
cd BMI_Calculator
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the project

```bash
python main.py
```

---

# 📊 BMI Formula

\[
BMI = \frac{Weight(kg)}{Height(m)^2}
\]

Example:

Weight = **70 kg**

Height = **1.75 m**

BMI = **22.86**

Category = **Normal Weight**



# 🚀 Future Improvements

Some additional features that can be added:

- Export history to CSV
- Delete individual records
- Edit existing records
- Dark Mode
- User Login System
- PDF Report Generation
- Print BMI Report
- Pie Chart for BMI Categories
- Monthly Statistics
- Custom Themes

---

# 🎯 Learning Outcomes

This project demonstrates practical knowledge of:

- Python Programming
- Tkinter GUI Development
- SQLite Database Management
- CRUD Operations
- Data Visualization using Matplotlib
- Input Validation
- Modular Programming
- Exception Handling

---

# 👨‍💻 Author

**Jaisal**

Second-Year Information Technology Student

Python | AI | Machine Learning | Full Stack Development

GitHub: https://github.com/Jaisal-21/OIBSIP

LinkedIn: https://www.linkedin.com/in/s-jaisal-b5ab1b329/

---

# 📜 License

This project is developed for educational purposes as part of the **Oasis Infobyte Python Development Internship**.

