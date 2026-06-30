import pandas as pd

df=pd.read_csv(r"C:\Users\Devansh Omar\OneDrive\Desktop\student.csv")
print(df.isnull())
print(df.isnull().sum())
print(df.duplicated())
print(df.duplicated().sum())
print(df.describe())
print(df.info())
print("memory_usage")
print(df.memory_usage())