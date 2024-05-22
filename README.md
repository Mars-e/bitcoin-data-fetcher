This script is your go-to tool for grabbing historical OHLCV (Open, High, Low, Close, Volume) data for the BTC/USDT trading pair from Binance. Whether you're into data analysis or backtesting your trading strategies, this script has got you covered.

What's Inside?
This script will:

Fetch historical OHLCV data for BTC/USDT at 15-minute intervals.
Allow you to input a custom date range (or use the default last month if you're feeling lazy).
Aggregate the data from multiple API requests to cover your specified date range.
Save all this juicy data into a CSV file right in your current working directory.

How to Use It:

Step 1: Install Dependencies
First things first, make sure you have the necessary libraries installed. If not, you can easily get them with pip:
pip install requests pandas python-dateutil

Step 2: Run the Script
Fire up your Python environment and run the script:
python 1_import_and_save_only.py

Step 3: Enter Date Range
When prompted, just enter the start and end dates in dd/mm/yyyy format. If you're fine with the default (one month prior to today), simply hit Enter.

Step 4: Check the Output
The script will work its magic and save the data as a CSV file named btc_usdt_ohlcv_data.csv in your current directory. If all goes well, you'll see a success message. If something's off, an error message will help you troubleshoot.

⏳ Note:
Fetching and saving the data might take a bit of time, so grab a coffee and relax. Don't worry if it seems like it's taking a while – the script is working hard for you! ☕🚀

Example
Here's a sneak peek at what you'll see:


Enter the start date (dd/mm/yyyy, default: 21/04/2024): 
Enter the end date (dd/mm/yyyy, default: 21/05/2024): 
Data has been successfully downloaded and saved to /your/current/directory/btc_usdt_ohlcv_data.csv.


The CSV file will have the following columns:

Date: Timestamp of the data point.
Open: Opening price at the start of the interval.
High: Highest price during the interval.
Low: Lowest price during the interval.
Close: Closing price at the end of the interval.
Volume: Volume of BTC traded during the interval.
CloseTime: Closing time of the interval.
QuoteAssetVolume: Volume of the quote asset traded during the interval.
NumberOfTrades: Number of trades that took place during the interval.
TakerBuyBaseAssetVolume: Volume of the base asset bought by takers.
TakerBuyQuoteAssetVolume: Volume of the quote asset bought by takers.
Ignore: Placeholder for additional data (not used).

A Final Note
This script is perfect for anyone diving into historical trading data. It's simple, efficient, and saves you a ton of time. Happy data analyzing and trading!

If you run into any issues or have suggestions for improvements, feel free to contribute or open an issue. Cheers! 🚀
