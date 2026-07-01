import pandas as pd

# Load cleaned dataset
df = pd.read_csv("output/cleaned_data.csv")
# 1. Top Performing Students
top_students = df[df["Marks"] >= 85]
top_students.to_csv("output/top_performing_students.csv", index=False)
# 2. Failed Students
failed_students = df[df["Marks"] <= 33]
failed_students.to_csv("output/failed_students.csv", index=False)
# 3. Students with Attendance below 75%
low_attendance = df[df["Attendance"] < 75]
low_attendance.to_csv("output/attendance_below_75.csv", index=False)
# 4. Students studying more than 8 hours
study_more_than_8 = df[df["StudyHours"] > 8]
study_more_than_8.to_csv("output/study_more_than_8_hours.csv", index=False)

print("✅ All filtered datasets have been saved successfully!")