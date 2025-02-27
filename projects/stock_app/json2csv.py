

import json
import pandas as pd

# Define the JSON file path
json_file = "stock_tickers.json"

with open(json_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# data typing check
# print(type(data))
# print(data.keys())

# Load JSON file
json_file = "stock_tickers.json"

with open(json_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# Extract the relevant data
meta_data = data.get("Meta Data", {})  # General stock information
time_series = data.get("Time Series (5min)", {})  # Time-based stock prices

# Convert time series data into a structured list
stock_records = []
for timestamp, values in time_series.items():
    record = {
        "timestamp": timestamp,
        "tickerSymbol": meta_data.get("2. Symbol", ""),  # Extract stock ticker
        "open": values.get("1. open", ""),
        "high": values.get("2. high", ""),
        "low": values.get("3. low", ""),
        "close": values.get("4. close", ""),
        "volume": values.get("5. volume", ""),
    }
    stock_records.append(record)

# Convert to DataFrame
df = pd.DataFrame(stock_records)

# Save to CSV
csv_file = "stock_data_2025_02_13.csv"
df.to_csv(csv_file, index=False)

print(f"Conversion complete: {csv_file} created.")
