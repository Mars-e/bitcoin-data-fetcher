import requests
import pandas as pd
from datetime import datetime, timedelta
import os
from dateutil.relativedelta import relativedelta
import time

# Get the current working directory
current_directory = os.getcwd()

# Calculate default date range (1 month prior to the current date to the current date)
end_date = datetime.now()
start_date = end_date - relativedelta(months=1)

# Ask the user for the date range or use the default
start_date_str = input(f"Enter the start date (dd/mm/yyyy, default: {start_date.strftime('%d/%m/%Y')}): ") or start_date.strftime('%d/%m/%Y')
end_date_str = input(f"Enter the end date (dd/mm/yyyy, default: {end_date.strftime('%d/%m/%Y')}): ") or end_date.strftime('%d/%m/%Y')

# Convert user input to datetime objects
start_date = datetime.strptime(start_date_str, "%d/%m/%Y")
end_date = datetime.strptime(end_date_str, "%d/%m/%Y")

# Binance API endpoint for klines (OHLCV data)
url = "https://api.binance.com/api/v3/klines"



# List to store data from multiple requests
all_data = []

# Define the time interval for each request (1 day)
interval = timedelta(days=1)

# Loop through the date range and make multiple requests
current_date = start_date
while current_date <= end_date:
    # Calculate timestamps for the API request
    start_timestamp = int(current_date.timestamp()) * 1000  # Convert to milliseconds
    end_timestamp = int((current_date + interval).timestamp()) * 1000  # Convert to milliseconds

    # Binance API parameters
    params = {
        "symbol": "BTCUSDT",
        "interval": "15m",  # 1 day interval
        "startTime": start_timestamp,
        "endTime": end_timestamp,
        "limit": 1000,  # Maximum limit per request
    }

    # Fetch the data from Binance
    response = requests.get(url, params=params)

    # Check if the API request was successful
    if response.status_code == 200:
        data = response.json()
        all_data.extend(data)
    else:
        print(f"Failed to fetch data for {current_date.strftime('%d/%m/%Y')}. Skipping...")

    # Move to the next date
    current_date += interval

# Create a DataFrame from the combined data
df = pd.DataFrame(all_data, columns=["timestamp", "open", "high", "low", "close", "volume", "close_time", "quote_asset_volume", "number_of_trades", "taker_buy_base_asset_volume", "taker_buy_quote_asset_volume", "ignore"])

# Convert the timestamp to a readable date format
df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")

# Rename columns
df.columns = ["Date", "Open", "High", "Low", "Close", "Volume", "CloseTime", "QuoteAssetVolume", "NumberOfTrades", "TakerBuyBaseAssetVolume", "TakerBuyQuoteAssetVolume", "Ignore"]

# Save the data to a CSV file in the current directory
csv_file = os.path.join(current_directory, "16_2_2024btc_usdt_ohlcv_data.csv")
df.to_csv(csv_file, index=False)

# Check if the CSV file is created and not empty
if df.empty:
    print("CSV file is empty. Data may not have been downloaded successfully.")
else:
    print(f"Data has been successfully downloaded and saved to {csv_file}.")
