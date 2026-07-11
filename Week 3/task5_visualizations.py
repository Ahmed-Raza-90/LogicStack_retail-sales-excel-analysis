import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
file_path = "Dataset/SCMS Delivery History Dataset.csv"

df = pd.read_csv(file_path)

# Convert Date Column
df["Delivered to Client Date"] = pd.to_datetime(
    df["Delivered to Client Date"],
    errors="coerce"
)

# Create Output Folder
import os

os.makedirs("charts", exist_ok=True)

# Chart 1
# Country vs Shipments (Bar Chart)
country_shipments = (
    df["Country"]
    .value_counts()
    .head(10)
)
plt.figure(figsize=(10,6))
plt.bar(country_shipments.index,
        country_shipments.values)
plt.title("Top 10 Countries by Shipments")
plt.xlabel("Country")
plt.ylabel("Total Shipments")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("charts/bar_country_shipments.png")
plt.show()

# Chart 2
# Shipment Mode Distribution (Pie Chart)
shipment_mode = df["Shipment Mode"].value_counts()
plt.figure(figsize=(8,8))
plt.pie(
    shipment_mode.values,
    labels=shipment_mode.index,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Shipment Mode Distribution")
plt.tight_layout()
plt.savefig("charts/pie_shipment_mode.png")
plt.show()

# Chart 3
# Delivery Trend Over Time (Line Chart)
delivery_trend = (
    df.groupby(
        df["Delivered to Client Date"].dt.to_period("M")
    )
    .size()
)
plt.figure(figsize=(12,6))
plt.plot(
    delivery_trend.index.astype(str),
    delivery_trend.values,
    marker="o"
)
plt.title("Delivery Trend Over Time")
plt.xlabel("Month")
plt.ylabel("Total Deliveries")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("charts/line_delivery_trend.png")
plt.show()

# Completed
print("="*60)
print("Charts Created Successfully!")
print("="*60)
print("Saved in charts folder:")
print()
print("1. bar_country_shipments.png")
print("2. pie_shipment_mode.png")
print("3. line_delivery_trend.png")