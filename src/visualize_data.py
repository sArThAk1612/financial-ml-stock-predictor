import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("tesla_stock_data.csv")


# convert Close column to numeric
df["Close"] = pd.to_numeric(df["Close"], errors="coerce")

# convert Date column
df["Date"] = pd.to_datetime(df["Date"])
df["Date"] = pd.to_datetime(df["Date"])
df["ma7"] = df["Close"].rolling(window=7).mean()
plt.figure(figsize=(12,6))

plt.plot(df["Date"], df["Close"], label="Tesla Close Price")
plt.plot(df["Date"], df["ma7"], label="7 Day Moving Average")

plt.title("Tesla Stock Price Trend")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()

plt.show()