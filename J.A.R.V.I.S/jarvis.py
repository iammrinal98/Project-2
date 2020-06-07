import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning Mrinal!')
    elif hour>=12 and hour<17:
        speak('Good Afternoon Mrinal!')    
    else:
        speak('Good Evening Mrinal!')

    speak('My name is Jarvis, how may i help you!')

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source) 

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f'You: {query}\n')

    except Exception as e:
        print(e)
        print("Sorry, I cann't get it")
        return "None"
    return query

    


if __name__=="__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia..one moment please')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https:\\www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("https:\\www.google.com")

        elif 'play music' in query:
            music_dir ='D:\\audio'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0])) 

        elif 'open chrome' in query:
            codePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath)

        elif 'open instagram' in query:
            webbrowser.open("https:\\www.instagram.com")  

        elif 'open github' in query:
            webbrowser.open("https:\\www.github.com")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Mrinal , the time is {strTime}") 

        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()  

    