import pandas as pd
import matplotlib.pyplot as plt

def get_top_publishers(news_df, top_n=10):
    return news_df['publisher'].value_counts().head(top_n)

def plot_publisher_frequency(news_df):
    publisher_counts = news_df['publisher'].value_counts().head(10)
    publisher_counts.plot(kind='bar', figsize=(10, 6))
    plt.title("Top Publishers by Article Count")
    plt.ylabel("Article Count")
    plt.xticks(rotation=45)
    plt.show()