import pandas as pd

# Load cleaned dataset
df = pd.read_csv("output/cleaned_data.csv")
# Students Sorted by Marks (Highest to Lowest)
print("=" * 70)
print("STUDENTS SORTED BY MARKS")
print("=" * 70)
sorted_marks = df.sort_values(by="Marks", ascending=False)
print(sorted_marks)
# Students Sorted by Attendance (Highest to Lowest)
print("\n" + "=" * 70)
print("STUDENTS SORTED BY ATTENDANCE")
print("=" * 70)
sorted_attendance = df.sort_values(by="Attendance", ascending=False)
print(sorted_attendance)
# Students Sorted by Study Hours (Highest to Lowest)
print("\n" + "=" * 70)
print("STUDENTS SORTED BY STUDY HOURS")
print("=" * 70)

sorted_study_hours = df.sort_values(by="StudyHours", ascending=False)
print(sorted_study_hours)