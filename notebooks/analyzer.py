import pandas as pd
from textblob import TextBlob

def get_sentiment_score(text):
    try:
        if pd.isna(text) or not isinstance(text, str) or text.strip() == "":
            return None
        return TextBlob(text).sentiment.polarity
    except Exception as e:
        print(f"Sentiment error on: {text} | {e}")
        return None

def apply_sentiment_analysis(news_df):
    news_df['sentiment'] = news_df['headline'].apply(get_sentiment_score)
    return news_df