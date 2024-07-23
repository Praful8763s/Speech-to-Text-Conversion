def main():
    text = speech_to_text()
    if text:
        sentiment = analyze_sentiment(text)
        if sentiment.polarity > 0:
            print("The sentiment of the speech is positive.")
        elif sentiment.polarity < 0:
            print("The sentiment of the speech is negative.")
        else:
            print("The sentiment of the speech is neutral.")

if __name__ == "__main__":
    main()
