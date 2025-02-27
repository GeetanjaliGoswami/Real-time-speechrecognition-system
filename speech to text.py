import speech_recognition as sr
import pyttsx3

# Initialize recognizer and engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text, language='en'):
    engine.setProperty('rate', 150)    # Speed percent (can go over 100)
    engine.setProperty('volume', 0.9)  # Volume 0-1
    voices = engine.getProperty('voices')
    
   
    if language == 'hi':  # Hindi
        engine.setProperty('voice', voices[1].id)
    elif language == 'ta':  # Tamil
        engine.setProperty('voice', voices[2].id)
    elif language == 'bn':  # Bengali
        engine.setProperty('voice', voices[3].id)
    elif language == 'kn':  # Kannada
        engine.setProperty('voice', voices[4].id)
    else:
        engine.setProperty('voice', voices[0].id)  # Default English voice
    
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech and convert to text
def recognize_speech(language='en'):
    with sr.Microphone() as source:
        print(f"Listening... (Speak in {language.upper()})")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
        try:
            print("Recognizing...")
            if language == 'hi':
                text = recognizer.recognize_google(audio, language='hi-IN')
            elif language == 'ta':
                text = recognizer.recognize_google(audio, language='ta-IN')
            elif language == 'bn':
                text = recognizer.recognize_google(audio, language='bn-IN')
            elif language == 'kn':
                text = recognizer.recognize_google(audio, language='kn-IN')
            else:
                text = recognizer.recognize_google(audio, language='en-US')  # Default to English
            
            print(f"You said: {text}")
            speak(text, language)
            
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

# Main loop
if __name__ == "__main__":
    while True:
        try:
            language = input("Enter language code (en for English, hi for Hindi, ta for Tamil, bn for Bengali, kn for Kannada): ").lower()
            recognize_speech(language)
        except KeyboardInterrupt:
            print("\nProgram terminated.")
            break
