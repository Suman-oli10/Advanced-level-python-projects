
import speech_recognition as sr
import webbrowser
import win32com.client
import musicLibrary

recognizer = sr.Recognizer()
speaker = win32com.client.Dispatch("SAPI.SpVoice")

def speak(text):
    print("jarvis:", text)
    speaker.Speak(text)

def processCommand(c):
    if "open google" in c.lower():
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    
    elif "open facebook" in c.lower():
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com") 
    
    elif "open youtube" in c.lower():
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com") 
        
    elif "open chatgpt " in c.lower():
        speak("Opening ChatGPT")
        webbrowser.open("https://www.chatgpt.com") 

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

if __name__ == "__main__":
    speak("Initializing jarvis....")
    while True:
    #Listen for the wake word "Jarvis"
    #obtain the word from the microphone
        r = sr.Recognizer()
        

        # recognize speech using Sphinx
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening!")
                audio = r.listen(source, timeout=3,phrase_time_limit=3)
            word=r.recognize_google(audio)

            if(word.lower()=="jarvis"):
                speak("Hajur Dai, I am listening")
                #listen for the command

                with sr.Microphone() as source:
                    print("jarvis is active")
                    audio = r.listen(source) 
                    command=r.recognize_google(audio)
                    processCommand(command)
        
        except Exception as e:
            print("Error; {0}".format(e))
