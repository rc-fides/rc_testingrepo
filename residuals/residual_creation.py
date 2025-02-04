import os
import shutil
import pandas as pd

# Define file paths
MAIN_CSV = "SheetA.csv"  # Replace with actual main CSV file path
AGENT_REPORTS_FOLDER = "Agent_Reports"  # Folder containing existing agent reports
OUTPUT_FOLDER = "XYZ_Month_Agent_Reports"  # New folder for updated reports

# Create output folder if it doesn't exist
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Load main CSV (Sheet A)
df_main = pd.read_csv(MAIN_CSV)

# Standardize column names (optional)
df_main.columns = df_main.columns.str.strip().str.lower()

# Function to process and update agent reports
def update_agent_report(agent_file):
    agent_path = os.path.join(AGENT_REPORTS_FOLDER, agent_file)
    df_agent = pd.read_csv(agent_path)

    # Standardize agent report column names
    df_agent.columns = df_agent.columns.str.strip().str.lower()

    # Merge main data with agent report based on account ID
    updated_df = df_main.merge(df_agent, on="account_id", how="outer", suffixes=("_main", "_agent"))

    # Remove obsolete accounts (those not in main CSV)
    updated_df = updated_df[updated_df["account_id"].isin(df_main["account_id"])]

    # Update financial columns
    updated_df["revenue"] = updated_df["revenue_main"].fillna(0)
    updated_df["transactions"] = updated_df["transactions_main"].fillna(0)
    updated_df["expenses"] = updated_df["expenses_main"].fillna(0)
    updated_df["residual"] = updated_df["revenue"] - updated_df["expenses"]  # Example formula

    # Select only necessary columns
    updated_df = updated_df[["account_id", "revenue", "transactions", "expenses", "residual"]]

    # Save updated report
    output_path = os.path.join(OUTPUT_FOLDER, agent_file)
    updated_df.to_csv(output_path, index=False)

# Process each agent report
for agent_file in os.listdir(AGENT_REPORTS_FOLDER):
    if agent_file.endswith(".csv"):
        update_agent_report(agent_file)

print("Agent reports updated and saved in:", OUTPUT_FOLDER)
