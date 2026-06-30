import pandas as pd

df = pd.read_csv("output/cleaned_data.csv")
df["Marks"] = pd.to_numeric(df["Marks"], errors="coerce")

# Grade function
def assign_grade(marks):
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

# NEW COLUMN CREATE
df["Grade"] = df["Marks"].apply(assign_grade)
df["Result"] = df["Marks"].apply(lambda x: "Pass" if x >= 33 else "Fail")
#performance Score
df["Performance_Score"] = (
    (df["Marks"] * 0.5) +
    (df["Attendance"] * 0.3) +
    (df["StudyHours"] * 0.2))
#performance level assing 
def performance(score):
    if score >= 85:
        return "Excellent"
    elif score >= 70:
        return "Good"
    elif score >= 50:
        return "Average"
    else:
        return "Poor"
df["Performance_Level"] = df["Performance_Score"].apply(performance)
print(df.head())
#saving the final output
df.to_csv("output/module4_transformed.csv", index=False)