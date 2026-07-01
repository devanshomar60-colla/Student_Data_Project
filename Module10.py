import os
import pandas as pd

df = pd.read_csv("output/cleaned_data.csv")

# Calculations
total_students = len(df)

passed_students = len(df[df["Result"] == "Pass"])
failed_students = len(df[df["Result"] == "Fail"])

highest_marks = df["Marks"].max()
lowest_marks = df["Marks"].min()
average_marks = df["Marks"].mean()

average_attendance = df["Attendance"].mean()

grade_distribution = df["Grade"].value_counts().reset_index()
grade_distribution.columns = ["Grade", "Count"]

# Create report
report_data = {
    "Metric": [
        "Total Students",
        "Passed Students",
        "Failed Students",
        "Highest Marks",
        "Lowest Marks",
        "Average Marks",
        "Average Attendance"
    ],
    "Value": [
        total_students,
        passed_students,
        failed_students,
        highest_marks,
        lowest_marks,
        round(average_marks, 2),
        round(average_attendance, 2)
    ]
}

report_df = pd.DataFrame(report_data)

# Save files
report_df.to_csv("output/report.csv", index=False)
grade_distribution.to_csv("output/grade_distribution.csv", index=False)

# Output
print("\n===== FINAL REPORT =====\n")
print(report_df)

print("\n===== GRADE DISTRIBUTION =====\n")
print(grade_distribution)

print("\n✅ SUCCESS: Module 10 Completed")