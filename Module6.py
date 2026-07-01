import pandas as pd

# Load cleaned dataset
df = pd.read_csv("output/cleaned_data.csv")
def grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "E"

df["Grade"] = df["Marks"].apply(grade)

# Create Result Column
df["Result"] = df["Marks"].apply(lambda x: "Pass" if x >= 40 else "Fail")

# Average Marks
average_marks = df["Marks"].mean()

# Highest Marks
highest_marks = df["Marks"].max()

# Lowest Marks
lowest_marks = df["Marks"].min()

# Average Attendance
average_attendance = df["Attendance"].mean()

# Average Study Hours
average_study_hours = df["StudyHours"].mean()

# Pass Percentage
pass_percentage = (df["Result"] == "Pass").mean() * 100

# Fail Percentage
fail_percentage = (df["Result"] == "Fail").mean() * 100

# Grade Distribution
grade_distribution = df["Grade"].value_counts()

# Print Results

print("========== STUDENT DATA ANALYSIS ==========\n")

print(f"Average Marks       : {average_marks:.2f}")
print(f"Highest Marks       : {highest_marks}")
print(f"Lowest Marks        : {lowest_marks}")
print(f"Average Attendance  : {average_attendance:.2f}")
print(f"Average Study Hours : {average_study_hours:.2f}")

print(f"\nPass Percentage : {pass_percentage:.2f}%")
print(f"Fail Percentage : {fail_percentage:.2f}%")

print("\nGrade Distribution")
print(grade_distribution)