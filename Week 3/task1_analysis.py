import pandas as pd

# Task 1: Load Dataset
# Dataset Path
file_path = "Dataset/SCMS Delivery History Dataset.csv"

# Load Dataset
df = pd.read_csv(file_path)

# Display First 10 Rows
print("=" * 60)
print("First 10 Rows")
print("=" * 60)

print(df.head(10))

# Check Dataset Shape
print("\n" + "=" * 60)
print("Dataset Shape")
print("=" * 60)

print(f"Rows    : {df.shape[0]}")
print(f"Columns : {df.shape[1]}")

# Display Column Names
print("\n" + "=" * 60)
print("Column Names")
print("=" * 60)

for i, column in enumerate(df.columns, start=1):
    print(f"{i}. {column}")

# Dataset Information
print("\n" + "=" * 60)
print("Dataset Information")
print("=" * 60)

df.info()

# Data Types
print("\n" + "=" * 60)
print("Data Types")
print("=" * 60)
print(df.dtypes)