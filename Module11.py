import os
import pandas as pd

# ================================
# STEP 1: Ensure output folder exists
# ================================
os.makedirs("output", exist_ok=True)

# ================================
# STEP 2: Load dataset
# ================================
df = pd.read_csv("output/cleaned_data.csv")

# ================================
# STEP 3: Create required datasets
# ================================

# Top performers (toppers)
toppers = df[df["Marks"] >= 85]

# Failed students
failed_students = df[df["Result"] == "Fail"]

# ================================
# STEP 4: Create final report data
# ================================
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
        len(df),
        len(df[df["Result"] == "Pass"]),
        len(df[df["Result"] == "Fail"]),
        df["Marks"].max(),
        df["Marks"].min(),
        round(df["Marks"].mean(), 2),
        round(df["Attendance"].mean(), 2)
    ]
}

report_df = pd.DataFrame(report_data)

# ================================
# STEP 5: Save ALL files in output folder
# ================================
df.to_csv("output/cleaned_data.csv", index=False)
toppers.to_csv("output/toppers.csv", index=False)
failed_students.to_csv("output/failed_students.csv", index=False)
report_df.to_csv("output/report.csv", index=False)

# ================================
# STEP 6: Display confirmation
# ================================
print("\n================ EXPORT COMPLETED ================\n")

print("✔ cleaned_data.csv saved")
print("✔ toppers.csv saved")
print("✔ failed_students.csv saved")
print("✔ report.csv saved")

print("\n🎉 All files successfully stored inside OUTPUT folder!")