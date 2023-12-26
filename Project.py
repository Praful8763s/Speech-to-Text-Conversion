# Import necessary libraries
import speech_recognition as sr
from googletrans import Translator
from flask import Flask, render_template, request

# Initialize Flask application
app = Flask(__name__)

# Initialize SpeechRecognition
recognizer = sr.Recognizer()

# Initialize Google Translator
translator = Translator()

# Function to perform speech-to-text conversion
def speech_to_text(audio_file):
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            return "Speech recognition could not understand audio"
        except sr.RequestError as e:
            return f"Could not request results from Google Speech Recognition service; {e}"

# Function to translate text to a specific language
def translate_text(text, target_language='en'):
    translation = translator.translate(text, dest=target_language)
    return translation.text

# Route to handle the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle the form submission
@app.route('/analyze', methods=['POST'])
def analyze():
    if 'audio_file' not in request.files:
        return "No audio file provided."

    audio_file = request.files['audio_file']
    if audio_file.filename == '':
        return "No selected audio file."

    # Perform speech-to-text conversion
    text_result = speech_to_text(audio_file)

    # Translate the text to English
    translated_text = translate_text(text_result)

    # Perform inmate behavior analysis (add your analysis code here)

    # Return the results to the frontend
    return render_template('result.html', original_text=text_result, translated_text=translated_text)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
