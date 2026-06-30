import pandas as pd

df=pd.read_csv(r"C:\Users\Devansh Omar\OneDrive\Desktop\student.csv")
print(df)
print(df.duplicated().sum())
'''duplicated() har row check karta hai.
Agar row pehle se exist karti hai to True deta hai.
sum() total duplicate rows count karta hai.
'''
df = df.drop_duplicates()#Duplicate rows ko hata deta hai.
print(df.duplicated().sum())
print(df.isnull().sum())
#filling missing values
df["StudyHours"] = df["StudyHours"].fillna(df["StudyHours"].mean())
df["Attendance"] = df["Attendance"].fillna(df["Attendance"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
df["Name"] = df["Name"].fillna("Unknown")
#validating attendance
df = df[(df["Attendance"] >= 0) & (df["Attendance"] <= 100)]
print(df)
#study hours validation
df = df[(df["StudyHours"] >= 0) & (df["StudyHours"]<=24)]
print(df)
#Marks validate
df = df[(df["Marks"] >= 0) & (df["Marks"] <= 100)]
print(df)
#saving cleaned dataset
df.to_csv("output/cleaned_data.csv", index=False)