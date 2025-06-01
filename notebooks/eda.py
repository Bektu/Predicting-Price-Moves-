import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_daily_news_volume(df):
    df['date_only'] = df['date'].dt.date
    daily_counts = df.groupby('date_only').size()

    plt.figure(figsize=(12, 5))
    daily_counts.plot()
    plt.title("News Headlines Volume Over Time")
    plt.ylabel("Number of Headlines")
    plt.xlabel("Date")
    plt.tight_layout()
    plt.show()

def plot_top_stocks(df, top_n=10):
    top_stocks = df['stock'].value_counts().head(top_n)

    plt.figure(figsize=(10, 4))
    sns.barplot(x=top_stocks.index, y=top_stocks.values)
    plt.title(f"Top {top_n} Most Mentioned Stocks")
    plt.ylabel("Headline Count")
    plt.xlabel("Stock Ticker")
    plt.tight_layout()
    plt.show()

def plot_publisher_distribution(df, top_n=10):
    top_publishers = df['publisher'].value_counts().head(top_n)

    plt.figure(figsize=(10, 4))
    sns.barplot(x=top_publishers.index, y=top_publishers.values)
    plt.title(f"Top {top_n} News Publishers")
    plt.ylabel("Headline Count")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_headline_length_distribution(df):
    df['headline_length'] = df['headline'].str.len()

    plt.figure(figsize=(10, 4))
    sns.histplot(df['headline_length'], bins=50, kde=True)
    plt.title("Distribution of Headline Lengths")
    plt.xlabel("Length (characters)")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()
