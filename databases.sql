CREATE DATABASES PROJECTS;
CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(15)
);

CREATE TABLE AudioFiles (
    audio_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    file_path VARCHAR(255),
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

CREATE TABLE Transcripts (
    transcript_id INT AUTO_INCREMENT PRIMARY KEY,
    audio_id INT,
    language VARCHAR(50),
    transcript_text TEXT,
    transcript_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (audio_id) REFERENCES AudioFiles(audio_id)
);

CREATE TABLE BehaviorAnalysis (
    analysis_id INT AUTO_INCREMENT PRIMARY KEY,
    transcript_id INT,
    analysis_result TEXT,
    analysis_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (transcript_id) REFERENCES Transcripts(transcript_id)
);
INSERT INTO Users (name, email, phone) VALUES ('John Doe', 'john@example.com', '1234567890');
INSERT INTO AudioFiles (user_id, file_path) VALUES (1, '/path/to/audio/file.mp3');
INSERT INTO Transcripts (audio_id, language, transcript_text) VALUES (1, 'Hindi', 'यह एक उदाहरण है');
INSERT INTO BehaviorAnalysis (transcript_id, analysis_result) VALUES (1, 'Positive sentiment detected');
SELECT * FROM Users;
SELECT * FROM BehaviorAnalysis WHERE transcript_id = 1;
SELECT * FROM Transcripts WHERE audio_id = 1;
