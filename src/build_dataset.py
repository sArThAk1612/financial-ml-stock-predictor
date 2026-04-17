import pandas as pd
import numpy as np

def build_dataset(stock_file):

    df = pd.read_csv(stock_file)

    # FIX: ensure numeric columns
    df["Close"] = pd.to_numeric(df["Close"], errors="coerce")
    df["Volume"] = pd.to_numeric(df["Volume"], errors="coerce")

    df = df.dropna()

    df["sentiment"] = np.random.uniform(-1,1,len(df))
    df["ma7"] = df["Close"].rolling(window=7).mean()
    df["price_change"] = df["Close"].pct_change()
    df["volatility"] = df["Close"].rolling(window=7).std()
# Regression target = tomorrow's closing price
    df["target"] = df["Close"].shift(-1)

    dataset = df[
        ["Close","Volume","sentiment","ma7","price_change","volatility","target"]
    ]

    dataset = dataset.dropna()

    dataset_file = "ml_dataset.csv"
    dataset.to_csv(dataset_file,index=False)

    return dataset_file