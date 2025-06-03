import pandas as pd
from scipy.stats import pearsonr

def merge_news_and_stock(news_df, stock_df):
    stock_df['Date'] = pd.to_datetime(stock_df['Date']).dt.date
    news_df['date'] = pd.to_datetime(news_df['date']).dt.date
    merged = pd.merge(news_df, stock_df, left_on=['stock', 'date'], right_on=['stock', 'Date'])
    return merged

def calculate_daily_returns(df):
    df = df.sort_values(['stock', 'Date'])
    df['daily_return'] = df.groupby('stock')['Close'].pct_change()
    return df

def calculate_correlation(df):
    df = df.dropna(subset=['sentiment', 'daily_return'])
    return pearsonr(df['sentiment'], df['daily_return'])
    