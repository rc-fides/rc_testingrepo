from dotenv import load_dotenv
import requests
import pandas as pd
import os

#modified script to load .env file
load_dotenv("keys.env")

#define API KEY
API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
if not API_KEY:
    raise ValueError("API key not found. You need to set environement variable for the API key.")

#API to get stock tickers:
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo'
response = requests.get(url)
#get list of stock tickers
print(response.status_code)  # Should be 200
print(response.text[:500])   # Print first 500 characters of the response



with open("stock_tickers.csv", "wb") as file:
    file.write(response.content)

# Read the CSV into a DataFrame
df = pd.read_csv("stock_tickers.csv")

# Display the first 5 rows
print(df.head())

# def get_real_time_price(symbol):
#     params = {
#         'function': 'GLOBAL_QUOTE',
#         'symbol': symbol,
#         'apikey': API_KEY
#     }
#     response = requests.get(BASE_URL, params=params)
#     data = response.json()
#     return data['Global Quote']['05. price']

# def get_historical_data(symbol, outputsize='compact'):
#     params = {
#         'function': 'TIME_SERIES_DAILY',
#         'symbol': symbol,
#         'outputsize': outputsize,
#         'apikey': API_KEY
#     }
#     response = requests.get(BASE_URL, params=params)
#     data = response.json()
#     df = pd.DataFrame.from_dict(data['Time Series (Daily)'], orient='index')
#     df = df.rename(columns={
#         '1. open': 'open',
#         '2. high': 'high',
#         '3. low': 'low',
#         '4. close': 'close',
#         '5. volume': 'volume'
#     })
#     df.index = pd.to_datetime(df.index)
#     df = df.astype(float)
#     return df

# watchlist = ['AAPL', 'MSFT', 'GOOGL']

# for symbol in watchlist:
#     print(f"Stock: {symbol}")
#     # Real-time price
#     current_price = get_real_time_price(symbol)
#     print(f"Current Price: ${current_price}")

#     # Historical data
#     historical_data = get_historical_data(symbol)
#     last_30_days = historical_data.head(30)

#     # Closing prices for the last 30 days
#     print("Last 30 Days Closing Prices:")
#     print(last_30_days['close'])

#     # 30-day high and low
#     high_30 = last_30_days['high'].max()
#     low_30 = last_30_days['low'].min()
#     print(f"30-Day High: ${high_30}")
#     print(f"30-Day Low: ${low_30}")

#     # 1-year high and low
#     full_data = get_historical_data(symbol, outputsize='full')
#     last_year = full_data.head(252)  # Approximate number of trading days in a year
#     high_1yr = last_year['high'].max()
#     low_1yr = last_year['low'].min()
#     print(f"1-Year High: ${high_1yr}")
#     print(f"1-Year Low: ${low_1yr}")
#     print("\n")

# fdsfs
#edits