from src.utils.io_utils import load_csv, save_csv
from src.sentiment.analyzer import apply_sentiment_analysis
from src.config import RAW_NEWS_PATH, PROCESSED_DATA_PATH

if __name__ == "__main__":
    news_df = load_csv(RAW_NEWS_PATH)
    news_df = apply_sentiment_analysis(news_df)
    save_csv(news_df, PROCESSED_DATA_PATH)
    print("Sentiment scores added and saved.")