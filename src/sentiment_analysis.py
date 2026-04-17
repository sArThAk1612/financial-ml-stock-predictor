import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
def analyze_sentiment(news_file):

    analyzer = SentimentIntensityAnalyzer()
    df = pd.read_csv(news_file)

    df["sentiment"] = df["headline"].apply(
        lambda x: analyzer.polarity_scores(x)["compound"]
    )

    avg_sentiment = df["sentiment"].mean()

    top_headline = df.iloc[df["sentiment"].idxmax()]["headline"]

    if avg_sentiment > 0.2:
        sentiment_label = "Positive"
    elif avg_sentiment < -0.2:
        sentiment_label = "Negative"
    else:
        sentiment_label = "Neutral"

    sentiment_file = "news_sentiment.csv"
    df.to_csv(sentiment_file, index=False)

    return sentiment_file, sentiment_label, top_headline