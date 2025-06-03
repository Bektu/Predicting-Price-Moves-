from textblob import TextBlob

def get_sentiment_score(text):
    return TextBlob(text).sentiment.polarity

def apply_sentiment_analysis(news_df):
    news_df['sentiment'] = news_df['headline'].apply(get_sentiment_score)
    return news_df