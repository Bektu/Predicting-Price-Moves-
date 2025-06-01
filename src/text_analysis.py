# text_analyser.py

from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def plot_top_ngrams(df, column='headline', n=20, ngram_range=(1,1)):
    vec = CountVectorizer(ngram_range=ngram_range, stop_words='english')
    ngrams = vec.fit_transform(df[column])
    counts = ngrams.sum(axis=0).A1
    vocab = vec.get_feature_names_out()
    
    top_indices = counts.argsort()[::-1][:n]
    top_ngrams = [(vocab[i], counts[i]) for i in top_indices]

    labels, values = zip(*top_ngrams)
    plt.figure(figsize=(10, 4))
    plt.barh(labels[::-1], values[::-1])
    plt.title(f"Top {n}-Grams")
    plt.tight_layout()
    plt.show()

def generate_wordcloud(df, column='headline'):
    text = " ".join(df[column].dropna())
    wc = WordCloud(width=800, height=400, background_color='white').generate(text)
    
    plt.figure(figsize=(12, 6))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.title("Headline Word Cloud")
    plt.show()
