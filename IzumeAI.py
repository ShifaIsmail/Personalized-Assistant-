import os
import speech_recognition as sr
import pyttsx3
import webbrowser
import time
import datetime
import openai
import random 
import numpy as np
import pyaudio
# print(pyaudio.__version__)
from config import apikey



chatStr = ""

def chat(query):

    global chatStr
    print(chatStr)

    openai.api_key = apikey
    chatStr += f" Author: {query}\n Izume:"

    response = openai.Completion.create(
        model="gpt-4o-mini-2024-07-18",
        prompt = chatStr,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]

    

def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for prompt: {prompt} \n"

    response = openai.Completion.create(
        model="gpt-4o-mini-2024-07-18",
        prompt = prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    text += response["choices"][0]["text"]
    if not os.path.exists("ai"):
        os.mkdir("ai")

    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
        f.write(text)

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    # os.system(f"say{text}")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold = 1
        # r.non_speaking_duration = 0.5
        audio = r.listen(source)
        try: 
            query = r.recognize_google(audio,language="en-in")
            print(f"User said: {query}")
            return query
        
        except sr.UnknownValueError:
            return "Sorry I didn't understand that"
        except sr.RequestError:
            return "Could not request result, check your network connection"
        except Exception as e:
            return "Am so sorry to say that there's an error. why not try saying something else"
        


if __name__=='__main__':
    engine = pyttsx3.init()
    say("Hi there! I am izume your A I assistant")
    while True:
        print("Listening...")
        query = takeCommand().lower()
        if query:
            command_found = False
        #     say(query)
        # if "Open Youtube".lower() in query.lower():
        #     webbrowser.open("https://youtube.com")
        #     say("let me take you to youtube tour")
            sites = [["youtube","https://www.youtube.com"],["wikipedia","https://www.wikipedia.com"],["google","https://www.google.com"],["instagram","https://www.instagram.com"],["snapchat","https://www.snapchat.com"],["twitter","https://www.x.com"],["chaptgpt","https://www.chatgpt.com"],["gemini","https://www.gemini.com"],["pinterest","https://www.pinterest.com"],["reddit","https://www.reddit.com"]]
            for site in sites:
                if f"Open {site[0]}" in query:
                    say(f"Let's look into {site[0]}")
                    webbrowser.open(site[1])
                    time.sleep(5)
                    break
            if "play instrument" in query:
                musicPath = "C:/Users/shifa/Music/E-guitarCover.mp3"
                os.startfile(musicPath)
            if "play music" in query:
                musicPath = "C:/Users/shifa/Music/Sleeping Child MLtR.mp3"
                os.startfile(musicPath)
            if "what's time" in query:
                strfTime = datetime.datetime.now().strftime("%H:%M:%S")
                say(f"it's {strfTime} on clock now ")
            if "exit" in query.lower() or "quit" in query.lower():
                say("Great talking to you. Goodbye!")
                break
            # response = chat(query)
            # print(f"Izume: {response} ")
            # say(response)

            # if command_found:
            #     time.sleep(2)
            elif "Using artificial intelligence" in query:
                ai(prompt=query)

            elif "Jarvis Quit" in query:
                exit()

            elif "reset chat" in query:
                chatStr = ""

            else:
                print("Chatting...")
                chat(query)