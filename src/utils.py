import yfinance as yf
import os
from alpha_vantage.timeseries import TimeSeries
import pandas as pd

def download_stock_data(ticker, start_date, end_date, folder='data'):
    """
    Download historical stock data from Yahoo Finance and save as CSV.
    """
    print(f"Downloading Yahoo Finance data for {ticker} from {start_date} to {end_date}...")
    data = yf.download(ticker, start=start_date, end=end_date)

    if data.empty:
        print(f"No Yahoo Finance data found for {ticker}.")
        return None

    os.makedirs(folder, exist_ok=True)
    filepath = os.path.join(folder, f"{ticker}_yahoo.csv")
    data.to_csv(filepath)
    print(f"Yahoo Finance data saved to {filepath}")

    return data

def download_alpha_vantage(ticker, start_date, end_date, folder='data', api_key='6YQ0FRF15S6WWZS4'):
    """
    Download stock data from Alpha Vantage and save as CSV.
    """
    print(f"Downloading Alpha Vantage data for {ticker}...")
    ts = TimeSeries(key=api_key, output_format='pandas')
    data, meta_data = ts.get_daily(symbol=ticker, outputsize='full')

    # Convert index to datetime
    data.index = pd.to_datetime(data.index)

    # Filter data by date range
    data = data[(data.index >= pd.to_datetime(start_date)) & (data.index <= pd.to_datetime(end_date))]

    if data.empty:
        print(f"No Alpha Vantage data for {ticker} in the given range.")
        return None

    os.makedirs(folder, exist_ok=True)
    filepath = os.path.join(folder, f"{ticker}_alpha.csv")
    data.to_csv(filepath)
    print(f"Alpha Vantage data saved to {filepath}")

    return data
