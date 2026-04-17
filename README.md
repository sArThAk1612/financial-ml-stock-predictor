# Financial ML Stock Predictor

A machine learning pipeline that predicts **next-day stock prices** using historical market data and **news sentiment analysis**.

This project combines **financial data, natural language processing, and machine learning** to generate an automated stock analysis report.

---

## Project Overview

Financial markets are influenced not only by historical price movements but also by news sentiment and macro information.

This project builds an end-to-end pipeline that:

1. Downloads historical stock price data
2. Collects latest financial news
3. Performs sentiment analysis on news headlines
4. Creates ML features
5. Trains a predictive model
6. Generates a prediction report

The final output provides an interpretable summary including predicted price movement and sentiment insights.

---

## Features

- Stock price data collection
- Financial news scraping
- News sentiment analysis
- Machine learning model training
- Next-day price prediction
- Automated prediction report

---

## Project Structure
financial-ml-stock-predictor
│
├── src/
│ ├── stock_data.py
│ ├── fetch_news.py
│ ├── sentiment_analysis.py
│ ├── train_model.py
│ ├── visualize_data.py
│
├── data/
│ tesla_stock_data.csv
│
├── notebooks/
│ stock_analysis.ipynb
│
├── requirements.txt
└── README.md
---

## Technologies Used

Python  
Pandas  
NumPy  
Scikit-learn  
Matplotlib  
News APIs / Web scraping  
Natural Language Processing (Sentiment Analysis)

---

## Machine Learning Pipeline

1️⃣ Fetch historical stock price data  

2️⃣ Collect recent news headlines  

3️⃣ Perform sentiment analysis on headlines  

4️⃣ Combine sentiment with price features  

5️⃣ Train machine learning model  

6️⃣ Predict next-day stock price  

---

## Example Output


Stock: TSLA

Current Price: $182.10
Predicted Price: $185.40
Expected Move: +1.81%

Confidence: 0.67

Sentiment Summary:
Mostly positive news sentiment

Top Headline:
"Tesla expands AI self-driving program"


---

## Future Improvements

- Backtesting trading strategy
- Trading signals (BUY / SELL / HOLD)
- Portfolio simulation
- Deep learning models (LSTM / Transformers)
- Real-time dashboard using Streamlit

---

