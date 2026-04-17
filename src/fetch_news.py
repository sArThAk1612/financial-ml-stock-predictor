import requests
import pandas as pd

def fetch_news(ticker):

    API_KEY = "233ea19f848f41b483e252c573b22ffb"

    url = f"https://newsapi.org/v2/everything?q={ticker}&language=en&sortBy=publishedAt&apiKey={API_KEY}"

    response = requests.get(url)

    data = response.json()

    # DEBUG: print API response if something fails
    if "articles" not in data:
        print("News API Error:", data)
        return None

    articles = data["articles"]

    news_list = []

    for article in articles:
        news_list.append({
            "date": article["publishedAt"][:10],
            "headline": article["title"]
        })

    news_df = pd.DataFrame(news_list)

    news_file = f"{ticker}_news.csv"

    news_df.to_csv(news_file, index=False)

    return news_file