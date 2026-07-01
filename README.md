# 📊 Student Data Management System

A Python + Pandas based project that performs student data cleaning, analysis, filtering, grouping, and visualization using CSV files.

This project demonstrates the practical use of **Python** and **Pandas** for data preprocessing and analysis.

---

## 🚀 Features

* Load student data from a CSV file
* Clean and preprocess data
* Assign Grades (A, B, C, D, E)
* Determine Pass / Fail status
* Calculate Performance Score
* Filter students based on different conditions
* Save filtered datasets into CSV files
* Perform GroupBy analysis
* Generate data visualizations

---

## 📂 Project Structure

```text
Student_Data_Project/
│
├── output/
│   ├── cleaned_data.csv
│   ├── top_performing_students.csv
│   ├── failed_students.csv
│   ├── attendance_below_75.csv
│   ├── study_more_than_8_hours.csv
│   ├── grade_summary.csv
│
├── student.csv
├── Module1.py
├── Module2.py
├── Module3.py
├── Module4.py
├── Module5.py
├── Module6.py
├── Module7.py
├── Module8.py
└── README.md
```

---

# 📘 Modules

## ✅ Module 1 – Load Dataset

* Import Pandas
* Load CSV file
* Display dataset
* Display first and last records
* Check rows and columns

---

## ✅ Module 2 – Data Cleaning

* Check missing values
* Remove duplicates
* Verify dataset
* Save cleaned dataset

---

## ✅ Module 3 – Data Transformation

* Assign Grades
* Assign Pass / Fail status
* Calculate Performance Score
* Save updated dataset

---

## ✅ Module 4 – Sorting & Filtering

* Sort students by Marks
* Filter students using conditions
* Display selected records

---

## ✅ Module 5 – Data Extraction

Create separate CSV files for:

* ⭐ Top Performing Students (Marks ≥ 85)
* ❌ Failed Students
* 📚 Students studying more than 8 hours
* 📉 Students with Attendance below 75%

---

## ✅ Module 6 – Statistical Analysis

Perform statistical analysis using Pandas:

* Mean Marks
* Maximum Marks
* Minimum Marks
* Average Attendance
* Total Students
* Pass Count
* Fail Count

---

## ✅ Module 7 – Data Visualization

Generate charts using Matplotlib:

* Marks Distribution
* Attendance Distribution
* Grade Count
* Study Hours vs Marks

---

## ✅ Module 8 – GroupBy Analysis

Using `groupby()`:

* Average Marks by Grade
* Number of Students in Each Grade
* Average Attendance by Grade

Example Output

| Grade | Average Marks | Students | Average Attendance |
| ----- | ------------: | -------: | -----------------: |
| A     |         91.80 |        8 |              94.25 |
| B     |         82.45 |       12 |              89.60 |
| C     |         73.15 |       10 |              84.10 |
| D     |         63.70 |        6 |              78.50 |
| E     |         45.25 |        4 |              70.00 |

---

## 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* CSV

---

## ▶️ How to Run

Clone the repository:

```bash
git clone https://github.com/devanshomar60-colla/Student_Data_Project.git
```

Move into the project folder:

```bash
cd Student_Data_Project
```

Install dependencies:

```bash
pip install pandas matplotlib numpy
```

Run any module:

```bash
python Module1.py
python Module2.py
python Module3.py
python Module4.py
python Module5.py
python Module6.py
python Module7.py
python Module8.py
```

---

## 📈 Learning Outcomes

This project demonstrates:

* CSV File Handling
* Data Cleaning
* Data Transformation
* Data Filtering
* Statistical Analysis
* GroupBy Operations
* Data Visualization
* File Handling using Pandas

---

## 👨‍💻 Author

Devansh Omar
