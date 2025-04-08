from utils import download_stock_data, download_alpha_vantage
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

def main():
    # Set date range (last 7 days)
    end_date = datetime.today()
    start_date = end_date - timedelta(days=7)

    start_date_str = start_date.strftime('%Y-%m-%d')
    end_date_str = end_date.strftime('%Y-%m-%d')

    ticker = 'TSLA'

    # Download data from Yahoo Finance
    data_yahoo = download_stock_data(ticker=ticker, start_date=start_date_str, end_date=end_date_str)

    # Download data from Alpha Vantage
    data_alpha = download_alpha_vantage(ticker=ticker, start_date=start_date_str, end_date=end_date_str, api_key='6YQ0FRF15S6WWZS4')

    # Plot comparison if both datasets are available
    if data_yahoo is not None and data_alpha is not None:
        plt.figure(figsize=(12, 6))
        plt.plot(data_yahoo.index, data_yahoo['Close'], label='Yahoo Finance', marker='o')
        plt.plot(data_alpha.index, data_alpha['4. close'], label='Alpha Vantage', marker='x')
        plt.title(f"{ticker} Closing Price Comparison (Last 7 Days)")
        plt.xlabel("Date")
        plt.ylabel("Closing Price (USD)")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    else:
        print("Data missing from one of the sources.")

if __name__ == '__main__':
    main()
