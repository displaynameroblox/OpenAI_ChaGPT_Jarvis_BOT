import pyttsx3 #Text to speech 
import datetime #Dt and Time
import speech_recognition as sr #speech recognition
import wikipedia #wikipedia
import webbrowser as wb
import os
import pyautogui
import psutil
import random
import pywin32_system32
import shutil
import ctypes
import subprocess
from urllib.request import urlopen
import openai
from config import apikey
from requests import get
import sys

#Test To Speech ----->
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 170)

#engine.say("Hello, this is Jarvis, What can I do for you")
#engine.runAndWait()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
#speak("Hello, this is Jarvis, What can I do for you")

def startup():
    print("Initializing Jarvis...")
    speak("Initializing Jarvis")
    print("Starting all systems applications")
    speak("Starting all systems applications")
    print("Installing and checking all drivers...")
    speak("Installing and checking all drivers")
    print("Caliberating and examining all the core processors")
    speak("Caliberating and examining all the core processors")
    print("Checking the internet connection...")
    speak("Checking the internet connection")
    print("Wait a moment sir")
    speak("Wait a moment sir")
    print("All drivers are up and running")
    speak("All drivers are up and running")
    print("All systems have been activated")
    speak("All systems have been activated")
    print("Now I am online")
    speak("Now I am online")

#Date And Time ----->
def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)
    print("The current time is ", Time)
#time()

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(day)
    speak(month)
    speak(year)
    print("The current date is " + str(day) + "/" + str(month) + "/" + str(year))
#date()

#Greetings ----->
def wishme():
    print("Welcome Back Sir !!!")
    speak("Welcome Back Sir !!!")
    #time()
    #date()
    hour = datetime.datetime.now().hour
    if hour>=6 and hour<=12:
        print("Good Morning Sir!!")
        speak("Good Morning Sir!!")
        
    elif hour>=12 and hour<18:
        print("Good Afternoon Sir!!")
        speak("Good Afternoon Sir!!")
        
    elif hour>=18 and hour<24:
        print("Good Evening Sir!!")
        speak("Good Evening Sir!!")
        
    else:
        speak("Good Night Sir")
        
    print("Jarvis at your service sir, please tell me how may I help you.")
    speak("Jarvis at your service sir, please tell me how may I help you.")
    
#wishme()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1    #wait for 1 sec
        audio = r.listen(source) #source =  microphone
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please")
        return "None"
        
    return query
   
def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at'+usage)
    battery = psutil.sensors_battery()
    speak('Battery is at')
    speak(battery.percent)
       
def username():
	speak("What should i call you sir")
	uname = takeCommand()
	speak("Welcome Mister")
	speak(uname)
	columns = shutil.get_terminal_size().columns
	
	print("#####################")
	print("Welcome Mr.", uname)
	print("#####################")
	
	speak("How can i Help you, sir")
 
def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for prompt: {prompt} \n ************************\n\n"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
    print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("OpenAI"):
        os.mkdir("OpenAI")
        
    #with open(f"OpenAI/prompt- {random.randint(1, 2343434356)}", 'w') as f:
    with open(f"OpenAI/{prompt[0:60]}.txt", 'w') as f:
        f.write(text)
chatStr=""

def chat(query):
    global chatStr
    openai.api_key = apikey
    chatStr += f"You: {query}\n Jarvis:"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatStr,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
    speak(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]
    
        
    #with open(f"OpenAI/prompt- {random.randint(1, 2343434356)}", 'w') as f:
    with open(f"OpenAI/{prompt[0:60]}.txt", 'w') as f:
        f.write(text)

#takeCommand()
#================================================================

#main
if __name__ == "__main__":
    startup()
    wishme()
    username()
    while True:
        query = takeCommand().lower()
        home_user_dir = os.path.expanduser("~")
        if 'time' in query:
            time()
            
        elif 'date' in query:
            date()
            
        elif "who are you" in query:
            speak("I'm JARVIS created by Mr. Kishan and I'm a desktop voice assistant.")
            print("I'm JARVIS created by Mr. Kishan and I'm a desktop voice assistant.")

        elif "how are you" in query:
            speak("I'm fine sir, What about you?")
            print("I'm fine sir, What about you?")

        elif "fine" in query:
            speak("Glad to hear that sir!!")
            print("Glad to hear that sir!!")

        elif "good" in query:
            speak("Glad to hear that sir!!")
            print("Glad to hear that sir!!")
            
        elif 'wikipedia' in query:
            try:
                speak("Ok wait sir, I'm searching...")
                query = query.replace("wikipedia","")
                result = wikipedia.summary(query, sentences=2)
                print(result)
                speak(result)
            except:
                speak("Can't find this page sir, please ask something else")
                
        elif "open youtube" in query:
            wb.open("youtube.com") 

        elif "open google" in query:
            print("Opening Google...?")
            print("What should i search on Google?")
            speak("What should i search on Google?")
            cm = takeCommand().lower()
            wb.open(f"{cm}") 
               
        elif 'what`s the time' in query:
            strTime = datetime.datetime.now().strftime("% H:% M:% S")
            speak(f"Sir, the time is {strTime}")
                  
        elif "change name" in query:
            speak("no i can't change, for that i have to take permission from mr. sahil lokhande")
                       
        elif "what's your name" in query or "what is your name" in query:
            print("I am Jarvis")
            speak("I am Jarvis")
            
        elif 'alexa' in query:
            speak("I don't know Alexa, but I've heard of Alexa. If you have Alexa, "
                        "I may have just triggered Alexa. If so, sorry Alexa.")

        elif 'google assistant' in query:
            speak("He was my classmate, too intelligent guy. We both are best friends.")

        elif 'siri' in query:
            speak("Siri, She's a competing virtual assistant on   a competitor's phone. "
                        "Not that I'm competitive or anything.")

        elif 'cortana' in query:
            speak("I thought you'd never ask. So I've never thought about it.")

        elif 'python assistant' in query:
            speak("Are you joking. You're coming in loud and clear.")

        elif 'what language you use' in query:
            speak("I am written in Python and I generally speak english.")
                  
        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Mr. Sahil Lokhande")
        
        elif "who i am" in query:
            speak("If you talk then definately your human.")
    
        elif "jarvis why you came to this world" in query:
            speak("Thanks to Mr. Sahil Lokhande who created me. further It's a secret and none of your business")
            
        elif 'what is love' in query:
            speak("It is 7th sense that destroy all other senses")
        
        elif "will you be my gf" in query or "will you be my bf" in query:
            speak("I'm not sure about, may be you should give me some time")
            
        elif "i love you" in query:
            speak("It's hard to understand")
            
        elif "Jarvis tell us about yourself" in query:
            speak("OK i am jarvis created by Mr. Sahil Lokahnde. i am virtual assistant.who can help you in your day today life.i can do virtually whatever you want.such as webbrowsing, opning applications,writing short notes.i can be your 24 by 7 assistant to help you sir.")
            
        elif 'open mozilla firefox' in query:
            os.startfile("C:\\Program Files\\Mozilla Firefox\\firefox.exe")

        elif 'open chrome' in query:
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

        elif 'close chrome' in query:
            os.system("TASKKILL /F /IM chrome.exe")
                  
        elif 'switch window' in query.lower() or 'change window' in query.lower():
            speak("Okay sir, Switching the window")
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
            
        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation() 
            
        elif 'shutdown system' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call(["shutdown", "/s"]) 
                           
        elif "open chrome" in query:
            print("Opening chrome....")
            chromePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromePath)
                
        elif 'search in chrome' in query:
            try:
                speak("what should I search?")
                print("What should I search?")
                chromepath = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
                search = takeCommand().lower()
                wb.get(chromepath).open_new_tab(search+'.com')
            except Exception as e:
                speak("Can't open now, please try again later.")
                print("Can't open now, please try again later.")
                
        elif 'clear browsing history' in query:
            pyautogui.hotkey('ctrl', 'shift', 'delete')
            
        elif 'close tab' in query:
            pyautogui.hotkey('ctrl', 'w')
            
        elif 'minimise this window' in query:
            pyautogui.hotkey('alt', 'space')
            time.sleep(1)
            pyautogui.press('n')
            
        elif 'open history' in query:
            pyautogui.hotkey('ctrl', 'h')
            
        elif 'open downloads' in query:
            pyautogui.hotkey('ctrl', 'j')

        elif 'open incognito window' in query:
            pyautogui.hotkey('ctrl', 'shift', 'n')
            
        elif "refresh" in query:
            pyautogui.moveTo(1551,551, 2)
            pyautogui.click(x=1551, y=551, clicks=1, interval=0, button='right')
            pyautogui.moveTo(1620,667, 1)
            pyautogui.click(x=1620, y=667, clicks=1, interval=0, button='left')
               
        elif 'logout' in query:
            print("Do you want to logout from your system?")
            speak("Do you want to logout from your system?")
            cmd = takeCommand()
            if 'no' in cmd:
                continue
            else:
                os.system("shutdown -l")
        
        elif 'shutdowm' in query:
            print("Do you want to shutdown you system?")
            speak("Do you want to shutdown you system?")
            cmd = takeCommand()
            if 'no' in cmd:
                continue
            else:
                os.system("shutdown /s /t 1")
            
        elif 'restart' in query:
            print("Do you want to restart your system?")
            speak("Do you want to restart your system?")
            cmd = takeCommand()
            if 'no' in cmd:
                continue
            else:
                os.system("shutdown /r /t 1")
            
        elif 'search google' in query:
            speak('What should I search?')
            search_term = takeCommand().lower()
            speak('Searching...')
            wb.open('https://www.google.com/search?q='+search_term)
                            
        elif 'using ai'.lower() in query.lower():
            ai(prompt = query)
        
        elif "go to sleep" in query:
            speak(' alright then, I am switching off')
            sys.exit()

        elif 'offline' in query:
            print("Bye !!! See you later")
            speak("Bye, See you later")
            quit()
            
        else:
            chat(query)
            
