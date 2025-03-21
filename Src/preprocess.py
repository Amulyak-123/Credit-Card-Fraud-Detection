import pandas as pd
from sklearn.preprocessing import StandardScaler
import os

# ✅ Load Dataset
df = pd.read_csv("Data/creditcard.csv")

# ✅ Print Initial Columns
print("✅ Columns before processing:", df.columns.tolist())

# ✅ Extract Time-Based Features
df["Transaction_Hour"] = (df["Time"] // 3600) % 24  # Convert to hours
df["Transaction_Day"] = (df["Time"] // (3600 * 24)) % 7  # Convert to days of the week
df["Time_Since_Last_Transaction"] = df["Time"].diff().fillna(0)  # Time difference between transactions
df["Peak_Hour"] = df["Transaction_Hour"].apply(lambda x: 1 if x in [12, 18, 20] else 0)  # Flag peak hours

# ✅ Detect Spending Anomalies
df["Rolling_Median_Amount"] = df["Amount"].rolling(window=5, min_periods=1).median()  # 5-transactions median
df["Spending_Spike"] = (df["Amount"] > df["Rolling_Median_Amount"] * 3).astype(int)  # Flag if spending is 3x usual

# ✅ Scale `Amount`
scaler = StandardScaler()
df["Amount_Scaled"] = scaler.fit_transform(df[["Amount"]])
df.drop(columns=["Amount", "Time"], inplace=True)  # Remove raw columns

# ✅ Print Columns After Processing
print("✅ Columns after processing:", df.columns.tolist())

# ✅ Save Processed Data
os.makedirs("data", exist_ok=True)
df.to_csv("Data/processed_data.csv", index=False)
print("✅ Data preprocessing complete! Saved as `data/processed_data.csv`.")
