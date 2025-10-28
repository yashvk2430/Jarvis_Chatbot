import speech_recognition as sr
import webbrowser
import pyttsx3
import music_library
import requests
from openai import OpenAI

recognizer=sr.Recognizer()
engine=pyttsx3.init()
newsapi="189266a0b42d49329c48adcc2df00835"
def speak(text):
    engine.say(text)
    engine.runAndWait()
def aiprocceser(command):
    client = OpenAI(
    api_key="sk-None-zrn1ir3QENdo5XQuBytiT3BlbkFJENNb0vSiNdlzilUIcbiE",
)
    completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": command}
  ]
)

    return completion.choices[0].message.content

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link= music_library.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r=requests.get("https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=189266a0b42d49329c48adcc2df00835")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
                speak(article['title'])
    else:
       output= aiprocceser(command)
       speak(output)

  

if __name__=="__main__":
    speak("initializing jarvis")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
         
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Ya")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)
        except Exception as e:
            print("Error; {0}".format(e))

