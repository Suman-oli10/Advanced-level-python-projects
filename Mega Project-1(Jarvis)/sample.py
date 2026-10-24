import speech_recognition as sr
import win32com.client
import webbrowser
import musicLibrary

# Initialize
recognizer = sr.Recognizer()
speaker = win32com.client.Dispatch("SAPI.SpVoice")

def speak(text):
    print("Mark:", text)
    speaker.Speak(text)

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You:", command)
        return command.lower()
    except:
        return ""

def process_command(command):

    if "google" in command:
        speak("Opening Google")
        webbrowser.open("https://google.com")

    elif "youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif "facebook" in command:
        speak("Opening Facebook")
        webbrowser.open("https://facebook.com")

    elif "chatgpt" in command:
        speak("Opening ChatGPT")
        webbrowser.open("https://chatgpt.com")

    elif command.startswith("play "):
        song = command.replace("play ", "").strip()

        if song in musicLibrary.music:
            speak(f"Playing {song}")
            webbrowser.open(musicLibrary.music[song])
        else:
            speak("Song not found")

if __name__ == "__main__":

    speak("Mark is ready")

    while True:

        wake_word = listen()

        if "hello" in wake_word:
            speak("Yes sir")
            print("After speaking")

        command = listen()

        if command:
            process_command(command)