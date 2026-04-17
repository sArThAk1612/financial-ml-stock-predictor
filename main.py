from src.stock_data import download_stock_data
from src.fetch_news import fetch_news
from src.sentiment_analysis import analyze_sentiment
from src.build_dataset import build_dataset
from src.train_model import train_model

def run_pipeline():

    ticker = input("Enter stock ticker: ")

    print("\nDownloading stock data...")
    stock_file = download_stock_data(ticker)

    print("\nFetching news...")
    news_file = fetch_news(ticker)

    print("\nRunning sentiment analysis...")
    sentiment_file, sentiment_label, top_headline = analyze_sentiment(news_file)

    print("\nBuilding ML dataset...")
    dataset_file = build_dataset(stock_file)

    print("\nTraining model...")
    result = train_model(dataset_file)

    print("\n-----------------------------")
    print("Stock:", ticker)
    print(f"\nCurrent Price: ${result['current_price']:.2f}")
    print(f"Predicted Price Tomorrow: ${result['predicted_price']:.2f}")
    print(f"Expected Move: {result['expected_move']:.2f}%")

    print(f"\nPrediction Confidence: {result['confidence']*100:.0f}%")

    print(f"\nNews Sentiment: {sentiment_label}")
    print("Top Headline:", top_headline)

    print(f"\nModel Accuracy (historical): {result['accuracy']:.2f}")
    print("-----------------------------")

if __name__ == "__main__":
    run_pipeline()