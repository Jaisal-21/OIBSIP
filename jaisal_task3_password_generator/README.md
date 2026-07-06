# 🔐 Random Password Generator

A modern **Python GUI application** that generates secure and customizable passwords using **Tkinter**. The application allows users to create strong passwords based on selected criteria, evaluate password strength, maintain password history, and export generated passwords for future reference.

---

## 📌 Features

- 🔑 Generate strong random passwords
- 📏 Select custom password length
- 🔠 Include uppercase letters
- 🔡 Include lowercase letters
- 🔢 Include numbers
- 🔣 Include special symbols
- 📊 Password strength indicator
- 📋 Copy password to clipboard
- 🗑️ Clear generated password
- 📅 Password history with Date and Time
- 📜 Scrollable password history table
- 💾 Export password history to CSV
- 🎨 Modern dark-themed GUI

---


---

## 📂 Project Structure

```
password_generator/
│
├── data/
│   └── history.txt
│
├── utils/
│   ├── generator.py
│   └── strength.py
│
├── main.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

## 🛠️ Technologies Used

- Python 3.x
- Tkinter
- ttk
- random
- string
- pyperclip
- csv
- datetime

---

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/password-generator.git
```

### Open the project folder

```bash
cd password-generator
```

### Install required package

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python main.py
```

---

## 📖 How to Use

1. Select the password length.
2. Choose the character types:
   - Uppercase
   - Lowercase
   - Numbers
   - Symbols
3. Click **Generate Password**.
4. Copy the generated password using the **Copy Password** button.
5. View previously generated passwords in the **Password History** table.
6. Export the history using the **Export** button.

---

## 🔐 Password Strength Levels

| Strength | Description |
|----------|-------------|
| Weak | Short password or limited character types |
| Medium | Good password with moderate complexity |
| Strong | Long password using multiple character sets |

---

## 📊 Password History

The application stores generated passwords locally in:

```
data/history.txt
```

Each record contains:

- Date
- Time
- Generated Password

Example:

```
29-06-2026 | 10:45:22 AM | Ab@91Xy#Lm
```

---

## 💾 Export Feature

Password history can be exported as a **CSV** file.

Example:

| Date | Time | Password |
|------|------|----------|
| 29-06-2026 | 10:45 AM | Ab@91Xy#Lm |

The exported CSV file can be opened using:

- Microsoft Excel
- Google Sheets
- LibreOffice Calc

---

## 📌 Future Improvements

- Light/Dark Theme Switch
- Password Generator Settings
- Password Search
- Password Statistics
- Save History to Database
- Password Encryption
- Auto Password Generator
- Custom Character Exclusion

---

## 👨‍💻 Author

**Jaisal**

Python Developer | AI Enthusiast

GitHub:
https://github.com/Jaisal-21/OIBSIP

LinkedIn:
https://www.linkedin.com/in/s-jaisal-b5ab1b329/

---

## 📄 License

This project is developed for educational and internship purposes.

