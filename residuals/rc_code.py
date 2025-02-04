import pandas as pd

# Define file path
file_path = "C:\Users\times\git\rc_testingrepo\python\residuals\2025_01_31_testfile.xlsx"
rc_code.py
# Load the Excel file and check available sheet names
xls = pd.ExcelFile(file_path)

xls.sheet_names

# Read through each file and then generate the output data in raw form
for agent_file in os.listdir(AGENT_REPORTS_FOLDER):
    if agent_file.endswith(".csv"):
        update_agent_report(agent_file)

#store output data into separate table
#do some dataframe shit TO the separate table data; that way the original dataset is in its untouched state (can be reverted and reuse the old data)

df_main = rd.read_rcgit 