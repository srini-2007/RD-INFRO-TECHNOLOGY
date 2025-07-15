
# 📂 RD INFRO TECHNOLOGY - Internship Task 2

## 📌 Task: File Handling and Data Processing

This project is a part of the Python internship offered by **RD INFRO TECHNOLOGY**. The objective of this task is to demonstrate basic file handling capabilities using Python by:

- Reading data from a CSV file
- Processing the data (removing missing values)
- Saving the cleaned data as a JSON file

---

## 📁 Project Structure

```
file_handling_task/
├── data.csv              # Input CSV file
├── file_process.py       # Python script for processing
├── output/
│   └── data.json         # Output JSON file
└── README.md             # Project documentation
```

---

## 🔧 Technologies Used

- Python 3.x
- pandas
- json
- os

---

## 🚀 How to Run the Project

### 🔹 Step 1: Install required module

```bash
pip install pandas
```

### 🔹 Step 2: Run the script

```bash
python file_process.py
```

This will:
- Read `data.csv`
- Remove rows with missing values
- Create `output/data.json`

---

## 📌 Sample Input: `data.csv`

```csv
name,age,city
Alice,25,New York
Bob,30,San Francisco
Charlie,,Los Angeles
David,28,Chicago
Eve,27,Boston
```

---

## 📦 Output: `data.json` (in output folder)

```json
[
    {
        "name": "Alice",
        "age": 25.0,
        "city": "New York"
    },
    {
        "name": "Bob",
        "age": 30.0,
        "city": "San Francisco"
    },
    {
        "name": "David",
        "age": 28.0,
        "city": "Chicago"
    },
    {
        "name": "Eve",
        "age": 27.0,
        "city": "Boston"
    }
]
```

---

## 🙋‍♂️ Author

P.Srinivasan
Intern at RD INFRO TECHNOLOGY

---

