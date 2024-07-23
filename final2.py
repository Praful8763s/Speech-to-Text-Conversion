import speech_recognition as sr
from textblob import TextBlob

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please speak something...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
    return None

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment
    print(f"Sentiment Analysis:\n Polarity: {sentiment.polarity}, Subjectivity: {sentiment.subjectivity}")
    return sentiment

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
