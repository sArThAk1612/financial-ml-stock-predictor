
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

def download_stock_data(ticker):

    end_date = datetime.today()
    start_date = end_date - timedelta(days=365*3)

    data = yf.download(ticker, start=start_date, end=end_date)

    data = data.reset_index()

    filename = f"{ticker}_stock_data.csv"
    data.to_csv(filename, index=False)

    print("Stock data saved:", filename)

    return filename