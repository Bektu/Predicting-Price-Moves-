from src.sentiment.analyzer import get_sentiment_score

def test_positive_sentiment():
    assert get_sentiment_score("Stock surges after earnings beat") > 0

def test_negative_sentiment():
    assert get_sentiment_score("Company hit by massive loss") < 0