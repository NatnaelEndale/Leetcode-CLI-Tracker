### 🧠 LeetCode CLI Tracker

A lightweight command-line application built with Python to track solved LeetCode problems.
This project focuses on clean CLI design, JSON-based data persistence, and modular Python code structure.

## 🚀 Features
- Add solved LeetCode problems via CLI commands
- Automatically saves the current date for each solved problem
- Persistently stores data in a JSON file
- List all solved problems in a structured format
- Handles empty data safely
- Simple and clean command-line interface using argparse

## 🛠 Tech Stack
- Python
- argparse – for building the command-line interface
- JSON – for data storage and persistence
- File I/O – reading and writing local data

## 📂 Project Structure
leetcode-tracker/<br/> 
│<br/>
├── main.py             # Entry point (CLI commands) and Core logic (add, list problems)<br/>
├── tracker.json        # Stores solved problems<br/>
└── README.md

## ⚙️ Usage
# ➕ Add a solved problem 
python main.py add --title "Two Sum" --difficulty Easy

# 📋 List all solved problems
python main.py list


If no problems are recorded, the program safely returns an empty list.

# 🧩 Example Stored Data (JSON)
[
  {
    "id": 567,
    "title": "Permutation in String",
    "difficulty": "Medium",
    "topic": "Sliding Window"
    "date": "2026-02-05"
  }
]

## 🧠 What I Learned
- How to design a command-line application in Python
- Using argparse to build structured CLI commands
- Persisting structured data using JSON
- Writing clean, modular, and readable Python code
- Handling edge cases like empty files and missing arguments

## 📈 Future Improvements
- Migrate data storage from JSON to SQLite
- Add statistics (problems solved by difficulty)
- Export data to CSV
- Add unit tests

## 👤 Author

Natnael Endale<br/>
Computer Science Student<br/>
Addis Ababa University
