import pandas as pd

# Load Cleaned Dataset
file_path = "Dataset/SCMS Delivery History Dataset.csv"
df = pd.read_csv(file_path)

# Convert Date Columns
date_columns = [
    "Scheduled Delivery Date",
    "Delivered to Client Date"
]
for col in date_columns:
    df[col] = pd.to_datetime(df[col], errors="coerce")

# Shipment Analysis
print("=" * 60)
print("SHIPMENT ANALYSIS")
print("=" * 60)

# Most Common Shipment Mode
most_common_mode = df["Shipment Mode"].mode()[0]
print("\nMost Common Shipment Mode:")
print(most_common_mode)

# Total Shipments Per Country
print("\nTotal Shipments Per Country:")
country_shipments = df["Country"].value_counts()
print(country_shipments)

# Delivery Performance
print("\n" + "=" * 60)
print("DELIVERY PERFORMANCE")
print("=" * 60)

# Calculate Delivery Delay
df["Delivery Delay (Days)"] = (
    df["Delivered to Client Date"] -
    df["Scheduled Delivery Date"]
).dt.days
print("\nFirst 10 Delivery Delays")

print(
    df[
        [
            "Scheduled Delivery Date",
            "Delivered to Client Date",
            "Delivery Delay (Days)"
        ]
    ].head(10)
)

# Average Delivery Time
average_delay = df["Delivery Delay (Days)"].mean()
print("\nAverage Delivery Delay:")
print(round(average_delay,2),"Days")

# Delayed Shipments
delayed = df[df["Delivery Delay (Days)"] > 0]
print("\nTotal Delayed Shipments:")
print(len(delayed))

# Cost Analysis
print("\n" + "=" * 60)
print("COST ANALYSIS")
print("=" * 60)

# Total Freight Cost
total_freight = df["Freight Cost (USD)"].sum()
print("\nTotal Freight Cost:")
print(round(total_freight,2))

# Average Line Item Value
average_value = df["Line Item Value"].mean()
print("\nAverage Line Item Value:")
print(round(average_value,2))

# Total Insurance Cost
total_insurance = df["Line Item Insurance (USD)"].sum()
print("\nTotal Insurance Cost:")
print(round(total_insurance,2))

# Summary
print("\n" + "=" * 60)
print("EDA COMPLETED SUCCESSFULLY")
print("=" * 60)
