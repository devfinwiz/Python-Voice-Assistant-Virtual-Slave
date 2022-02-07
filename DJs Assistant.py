from more_itertools import take
import pyttsx3 
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import time
import pyjokes
import winshell

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id) # 0 for male, 1 for female voice

def go_deaf():
            speak("For how long should I not listen?Specify a number in seconds, for example 10")
            a = int(accept_input())
            time.sleep(a)
            a=str(a)
            speak("I am back after pretending to be deaf for "+a+"seconds")

def initial_greetings():
    hour=int(datetime.datetime.now().hour)

    if (hour>=0 and hour<=12):
        speak("Wake up, it's time to get going!!")
    elif(hour>=12 and hour<=18):
        speak("Afternoon, get going!")
    else:
        speak("Evening, get going!")

    speak("What are you looking for?")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def accept_input():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening to you...")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing your input....")
        query=r.recognize_google(audio,language='en-in')
        print(f"You spoke: {query}\n")

    except Exception as e:
        print("Encountered some problem, say it again please")
        return "None"

    return query

def sendEmail(to, content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your email id here','your password here')
    server.sendmail('your email id here',to,content)
    server.close()

def browser_access(url):
    webbrowser.open_new_tab(url)

def write_note():
            speak("What should i write, sir")
            note = accept_input()
            file = open('Note.txt', 'w')
            file.write(note)
            speak("Done sir, find your written note in the same working directory!")

if __name__=='__main__':
    initial_greetings()

    while True:
        query=accept_input().lower()

        if query==0:
            continue

        if 'wikipedia' in query:
            speak('Searching for wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=3)
            speak("According to wikipedia ")
            print(results)
            speak(results)

        if 'open notepad' in query:
            npath="C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)

        elif 'write a note' in query:
            write_note()

        elif "show note" in query:
            speak("Showing Notes")
            file = open("Note.txt", "r")
            print(file.read())
            speak("Kindly watch the note contents printed on your terminal")

        elif "don't listen" in query or "stop listening" in query:
            go_deaf()

        elif 'empty recycle bin' in query:
            speak("On it!")
            winshell.recycle_bin().empty(confirm = False, show_progress = True, sound = True)
            speak("Recycle Bin Recycled")

        elif 'open paint' in query:
            npath="C:\\Windows\\system32\\mspaint.exe"
            os.startfile(npath)

        elif 'open youtube' in query:
            browser_access("youtube.com")

        elif 'open google' in query:
            browser_access("google.com")

        elif 'time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Current time is {strtime}")

        elif 'open carryminati youtube channel' in query:
           browser_access("https://www.youtube.com/channel/UCj22tfcQrWG7EMEKS0qLeEg")
        
        elif 'open linkedin' in query:
            browser_access("linkedin.com")

        elif 'email to a friend' in query:
            try:
                speak("Speak up your content")
                content=accept_input()
                to="receiver's email id"
                sendEmail(to,content)
                speak("Email sent successfully")

            except Exception as e:
                print(e)
                speak("Encountered error while sending email, sorry!")

        elif 'bye' in query or 'shutdown' in query or 'tata' in query:
            speak("Your assistant is shutting down, goodbye")
            print("Your assistant is shutting down, goodbye")
            break

        elif 'news' in query:
            speak("I've got Hindustan times and Economic times for you")
            browser_access("https://www.hindustantimes.com/")
            browser_access("https://economictimes.indiatimes.com/")
            speak("Enjoy reading")

        elif 'open' in query:
            query = query.replace("open", "")
            browser_access(query)
            time.sleep(5)	

        elif 'nothing' in query:
            speak("Should I stop listening then? ")
            hold=accept_input()

            if 'yes' in hold:
                go_deaf()
            else:
                speak("Okay, on standby then! Still listening to you without causing any disturbance!")
                
        elif 'joke' in query:
            speak(pyjokes.get_joke())

        
        '''elif 'who are you' or 'introduce' in query:
            speak("I am DevFinwiz's Assistant")
            print("I am DevFinwiz's Assistant")'''

        

        



        



