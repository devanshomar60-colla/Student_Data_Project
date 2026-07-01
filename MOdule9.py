import pandas as pd

# Load dataset
df = pd.read_csv("output/cleaned_data.csv")

# ----------------------------
# 1. Mean
# ----------------------------
mean_values = df[["Marks", "Attendance", "StudyHours"]].mean()

# ----------------------------
# 2. Median
# ----------------------------
median_values = df[["Marks", "Attendance", "StudyHours"]].median()

# ----------------------------
# 3. Mode
# ----------------------------
mode_values = df[["Marks", "Attendance", "StudyHours"]].mode()

# ----------------------------
# 4. Standard Deviation
# ----------------------------
std_values = df[["Marks", "Attendance", "StudyHours"]].std()

# ----------------------------
# 5. Variance
# ----------------------------
var_values = df[["Marks", "Attendance", "StudyHours"]].var()

# ----------------------------
# 6. Correlation Matrix
# ----------------------------
correlation_matrix = df[["Marks", "Attendance", "StudyHours"]].corr()

# ----------------------------
# PRINT RESULTS
# ----------------------------
print("\n📊 MEAN VALUES:\n", mean_values)

print("\n📊 MEDIAN VALUES:\n", median_values)

print("\n📊 MODE VALUES:\n", mode_values)

print("\n📊 STANDARD DEVIATION:\n", std_values)

print("\n📊 VARIANCE:\n", var_values)

print("\n📊 CORRELATION MATRIX:\n", correlation_matrix)

# ----------------------------
# SAVE OUTPUT FILES
# ----------------------------
mean_values.to_csv("output/mean_values.csv")
median_values.to_csv("output/median_values.csv")
mode_values.to_csv("output/mode_values.csv")
std_values.to_csv("output/std_values.csv")
var_values.to_csv("output/variance_values.csv")
correlation_matrix.to_csv("output/correlation_matrix.csv")