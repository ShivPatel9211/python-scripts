import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import datetime
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recogining...")
            data = recognizer.recognize_google(audio)
            return data
        except sr.UnknownValueError:
            error="Not Understand"
            return error

def text_to_speech(text):
    engine = pyttsx3.init()
    voices= engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 120)
    engine.say(text)
    engine.runAndWait()

if __name__=="__main__":
    if speech_to_text().lower() == 'hello':
        text_to_speech("Hey, How can i help you?")
        data1=''
        while data1!="close":
            data1=speech_to_text().lower()
            if "your name" in data1:
                name="My name is Buddy"
                text_to_speech(name)
            elif 'old are you' in data1:
                age="I am 10 years old"
                text_to_speech(age)
            elif'youtube' in data1:
                webbrowser.open('https://www.youtube.com/')
                exit()
            elif 'have girlfriend' in data1 or 'have boyfriend' in data1:
                text_to_speech("I am machine, so I didn't have any feeling.")
            elif 'i love you' in data1:
                text_to_speech('I love you too')
            elif 'play hindi song' in data1:
                webbrowser.open("https://www.youtube.com/results?search_query=hindi+song")
                exit()
            # elif 'play song' in data1:
            #     add="F:\song hindiii\hindi_song"
            #     songs=os.listdir(add)
            #     os.startfile(os.path.join(add,songs[2]))
            #     exit()
            elif data1=='close':
                text_to_speech("thank you for using me, bye have a nice day")
            elif "who is nitesh" in data1:
                text_to_speech("Nitesh is your brother")
            elif 'do you know hindi' in data1:
                text_to_speech("Sorry dear, I can understand only english")
            elif 'who is my girlfriend' in data1:
                text_to_speech("Sheetal is your girlfriend, but she is Bhootani")
            elif data1=="not understand":
                text_to_speech("I am listening, Please command me.")
            elif 'show my photo' in data1:
                path=r"C:\Users\spate\OneDrive\Pictures\profile.jpeg"
                os.startfile(path)
                exit()
            elif 'time' in data1:
                time = datetime.datetime.now().strftime("%I%M%p")
                text_to_speech(f'time is {time}')
            elif 'date' in data1:
                date = datetime.datetime.now().strftime("%A%M%Y")
                text_to_speech(f'date is {date}')
            # elif 'open this pc' in data1:
            #     path=r"C:\Users\spate\This PC - Shortcut.Ink"
            #     os.startfile(path)
            else:
                if data1 == "":
                    text_to_speech(f"Sorry , I didn't understand. If your want stop me please say close.")
                else:
                    text_to_speech("This is matching result from google")
                    webbrowser.open("https://google.com/search?q=%s" % data1) 
    else:
        text_to_speech("To start me please say hello")