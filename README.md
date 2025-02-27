# speech

This project demonstrates the integration of speech recognition and text-to-speech (TTS) technologies to create a multilingual voice assistant prototype. It supports multiple languages, including English, Hindi, Tamil, Bengali, and Kannada. The program listens to the user's voice input, converts it to text, and then speaks the text back in the selected language.

Features
Speech Recognition:

Captures audio input from the microphone.

Converts speech to text using Google Speech Recognition API.

Supports multiple languages: English (en), Hindi (hi), Tamil (ta), Bengali (bn), and Kannada (kn).

Text-to-Speech (TTS):

Converts text to speech using pyttsx3 (offline) or gTTS (online).

Customizable speech rate and volume.

Supports multiple languages and voices.

Multilingual Support:

Recognizes and speaks in the selected language.

Easy language selection via command-line input.

Interactive Command-Line Interface:

Continuously listens for user input.

Can be terminated using Ctrl+C.

Libraries Used
speech_recognition:

Captures audio from the microphone and converts speech to text.

Supports multiple languages via Google Speech Recognition API.

pyttsx3:

Offline text-to-speech library.

Customizable voice, speed, and volume.

gTTS (Google Text-to-Speech):

Online text-to-speech library.

Generates audio files (e.g., MP3) from text.

os:

Plays generated audio files using the system's default media player.

How It Works
The user selects a language by entering a language code (e.g., en for English, hi for Hindi).

The program listens to the user's voice input through the microphone.

The speech is recognized and converted to text using Google Speech Recognition.

The recognized text is spoken back to the user in the selected language using pyttsx3 or gTTS.

The program runs in a loop, allowing continuous interaction until terminated by the user.

Installation
Clone the repository:

bash
Copy
git clone https://github.com/your-username/multilingual-speech-tts.git
cd multilingual-speech-tts
Install the required libraries:

bash
Copy
pip install SpeechRecognition pyttsx3 gtts
Run the program:

bash
Copy
python main.py
Usage
Run the program:

bash
Copy
python main.py
Enter a language code when prompted:

en for English

hi for Hindi

ta for Tamil

bn for Bengali

kn for Kannada

Speak into the microphone when prompted. The program will recognize your speech and respond in the selected language.

To exit the program, press Ctrl+C.

Example
plaintext
Copy
Enter language code (en for English, hi for Hindi, ta for Tamil, bn for Bengali, kn for Kannada): hi
Listening... (Speak in HI)
Recognizing...
You said: नमस्ते
The program will then speak "नमस्ते" in Hindi.
