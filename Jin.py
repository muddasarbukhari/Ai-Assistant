import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import wikipedia
import os
import random


'''Initialize the engine.'''
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    '''Function to convert text to speech'''
    engine.say(audio)
    engine.runAndWait()

def greetings():
    '''This function is for greeting the user'''
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak ("Good Morning!")
    elif hour >= 12 and hour <18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Jin. Sir, how may I help you?")

def userinput():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        
        audio = r.listen(source)
    try:
     print("Recognizing....")
     query = r.recognize_google(audio, language='en-PK')
     print(f"you said: {query}\n")
    except Exception as e:
      print(e)
      return "None"
    return query

if __name__ == "__main__":
     greetings()
     
     while True:
        query = userinput().lower()
     
        # Logic for executing task based on query
        if 'youtube' in query:
            c = webbrowser.get('windows-default')
            c.open('https://www.youtube.com/')
            speak("Opening Youtube")


        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak ("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'google' in query:
             c = webbrowser.get('windows-default')
             c.open('https://www.google.com/')
             speak("Opening Google")

        elif 'play music' in query:
            num = random.randint(0, 332)

            music_dir = 'Path of your music folder'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[num]))
            speak("Playing Music")
        
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open Wordpad' in query:
            wordPath = "Path of your text editor here like Microsoft Word"
            os.startfile(wordPath)
            speak("Opening wordpad")
            try:
                speak("What should I write?")
                content = userinput()
            except Exception as e:
                speak("Sorry sir, I was not able to write. Please try again")
        
        elif 'open code' in query:
            codePath = "Path of your text editor which you prefer for coding"
            os.startfile(codePath)
        
        elif 'videos' in query:
            num = random.randint(0, 71)
            video_Folder = "Path of your videos folder here"
            videos = os.listdir(video_Folder)
            os.startfile((os.path.join(video_Folder, videos[num])))
            speak("Playing videos")


        else:
            print("I could not understand, Sir, please try again.")
            speak("I could not understand, Sir, please try again.")