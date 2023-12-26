import speech_recognition as sr
import pymysql

# MySQL Connection Configuration
db_host = "your_mysql_host"
db_user = "your_mysql_user"
db_password = "your_mysql_password"
db_database = "your_mysql_database"


# Function to convert speech to text using Google Web Speech API
def speech_to_text(audio_file):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio_data, language="en-IN")  # Adjust language code as per requirement
        return text
    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None


# Function to store data in MySQL
def store_in_mysql(text):
    connection = pymysql.connect(host=db_host, user=db_user, password=db_password, database=db_database)
    cursor = connection.cursor()

    # Adjust the SQL query based on your database schema
    sql_query = "INSERT INTO inmate_behavior_analysis (text) VALUES (%s)"

    try:
        cursor.execute(sql_query, (text,))
        connection.commit()
        print("Data successfully stored in MySQL.")
    except pymysql.Error as e:
        print(f"Error storing data in MySQL: {e}")
    finally:
        cursor.close()
        connection.close()


# Example usage
if __name__ == "__main__":
    audio_file_path = "path_to_your_audio_file.wav"  # Provide the path to the audio file

    # Convert speech to text
    extracted_text = speech_to_text(audio_file_path)

    if extracted_text:
        # Store the text in MySQL
        store_in_mysql(extracted_text)
