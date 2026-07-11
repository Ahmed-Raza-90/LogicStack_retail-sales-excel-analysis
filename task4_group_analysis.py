import pandas as pd

# Load Dataset
file_path = "Dataset/SCMS Delivery History Dataset.csv"
df = pd.read_csv(file_path)

# Convert Date Columns
df["Scheduled Delivery Date"] = pd.to_datetime(
    df["Scheduled Delivery Date"],
    errors="coerce"
)
df["Delivered to Client Date"] = pd.to_datetime(
    df["Delivered to Client Date"],
    errors="coerce"
)

# Convert Freight Cost to Numeric
df["Freight Cost (USD)"] = pd.to_numeric(
    df["Freight Cost (USD)"],
    errors="coerce"
)
df["Freight Cost (USD)"] = df["Freight Cost (USD)"].fillna(0)

# Calculate Delivery Delay
df["Delivery Delay (Days)"] = (
    df["Delivered to Client Date"]
    - df["Scheduled Delivery Date"]
).dt.days

# GROUP 1
# Country vs Total Shipments
print("=" * 70)
print("Country vs Total Shipments")
print("=" * 70)

country_shipments = (
    df.groupby("Country")
      .size()
      .sort_values(ascending=False)
)
print(country_shipments)

# GROUP 2
# Vendor vs Total Cost
print("\n" + "=" * 70)
print("Vendor vs Total Freight Cost")
print("=" * 70)
vendor_cost = (
    df.groupby("Vendor")["Freight Cost (USD)"]
      .sum()
      .sort_values(ascending=False)
)
print(vendor_cost)

# GROUP 3
# Product Group vs Total Value
print("\n" + "=" * 70)
print("Product Group vs Total Line Item Value")
print("=" * 70)
product_value = (
    df.groupby("Product Group")["Line Item Value"]
      .sum()
      .sort_values(ascending=False)
)
print(product_value)

# GROUP 4
# Shipment Mode vs Average Delay
print("\n" + "=" * 70)
print("Shipment Mode vs Average Delivery Delay")
print("=" * 70)
shipment_delay = (
    df.groupby("Shipment Mode")["Delivery Delay (Days)"]
      .mean()
      .sort_values()
)
print(shipment_delay)

# Task Completed
print("\n" + "=" * 70)
print("GROUP ANALYSIS COMPLETED SUCCESSFULLY")
print("=" * 70)
