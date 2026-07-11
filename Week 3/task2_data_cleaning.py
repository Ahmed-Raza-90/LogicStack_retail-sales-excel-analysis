import pandas as pd

# Load Dataset
file_path = "Dataset/SCMS Delivery History Dataset.csv"

df = pd.read_csv(file_path)

# STEP 1: Convert Date Columns
date_columns = [
    "PQ First Sent to Client Date",
    "PO Sent to Vendor Date",
    "Scheduled Delivery Date",
    "Delivered to Client Date",
    "Delivery Recorded Date"
]

for col in date_columns:
    df[col] = pd.to_datetime(df[col], errors="coerce")

print("="*60)
print("Date Conversion Completed")
print("="*60)

print(df[date_columns].dtypes)

# STEP 2: Check Missing Values
print("\n" + "="*60)
print("Missing Values")
print("="*60)

missing = df.isnull().sum()
print(missing[missing > 0])

# STEP 3: Handle Missing Values
# Shipment Mode -> Fill with Most Frequent Value
df["Shipment Mode"] = df["Shipment Mode"].fillna(
    df["Shipment Mode"].mode()[0]
)

# Dosage -> Fill with Unknown
df["Dosage"] = df["Dosage"].fillna("Unknown")

# Insurance -> Fill with 0
df["Line Item Insurance (USD)"] = df["Line Item Insurance (USD)"].fillna(0)

print("\nMissing Values After Filling")
print(df.isnull().sum()[df.isnull().sum() > 0])

# STEP 4: Convert Numeric Columns
# Freight Cost
df["Freight Cost (USD)"] = pd.to_numeric(
    df["Freight Cost (USD)"],
    errors="coerce"
)

# Replace NaN with 0
df["Freight Cost (USD)"] = df["Freight Cost (USD)"].fillna(0)

# Weight
df["Weight (Kilograms)"] = pd.to_numeric(
    df["Weight (Kilograms)"],
    errors="coerce"
)
df["Weight (Kilograms)"] = df["Weight (Kilograms)"].fillna(
    df["Weight (Kilograms)"].median()
)

# Unit Price
df["Unit Price"] = pd.to_numeric(
    df["Unit Price"],
    errors="coerce"
)

# Final Dataset Information
print("\n" + "="*60)
print("Final Data Types")
print("="*60)

print(df.dtypes)

print("\n" + "="*60)
print("Remaining Missing Values")
print("="*60)

print(df.isnull().sum())

# Save Cleaned Dataset
df.to_csv("Dataset/SCMS Delivery History Dataset.csv", index=False)

print("\n" + "="*60)
print("Data Cleaning Completed Successfully!")
print("Cleaned dataset saved as:")
print("Dataset/SCMS Delivery History Dataset.csv")
print("="*60)