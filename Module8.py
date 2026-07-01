import pandas as pd

# Load cleaned dataset
df = pd.read_csv("output/cleaned_data.csv")
# Grade Function
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

# Add Grade Column
df["Grade"] = df["Marks"].apply(assign_grade)

# Add Result Column
df["Result"] = df["Marks"].apply(lambda x: "Pass" if x >= 40 else "Fail")

# Save updated dataset
df.to_csv("output/cleaned_data.csv", index=False)
print(df)