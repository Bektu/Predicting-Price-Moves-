import pandas as pd
import matplotlib.pyplot as plt

def plot_headline_lengths(news_df):
    news_df['headline_length'] = news_df['headline'].apply(len)
    news_df['headline_length'].hist(bins=30, figsize=(10, 6))
    plt.title("Distribution of Headline Lengths")
    plt.xlabel("Length")
    plt.ylabel("Frequency")
    plt.show()