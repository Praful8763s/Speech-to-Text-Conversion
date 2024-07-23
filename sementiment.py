from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment
    print(f"Sentiment Analysis:\n Polarity: {sentiment.polarity}, Subjectivity: {sentiment.subjectivity}")
    return sentiment
