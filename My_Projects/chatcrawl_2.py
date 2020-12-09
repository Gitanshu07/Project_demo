from datetime import datetime
import bs4 as bs4
import urllib.request as url
from gtts import gTTS
import pygame

pygame.mixer.init()

print("Welcome",name := input("Enter your name : "))

import speech_recognition as sr


mic_name = "USB Device 0x46d:0x825: Audio (hw:1, 0)"
sample_rate = 48000
chunk_size = 2048
r = sr.Recognizer()

mic_list = sr.Microphone.list_microphone_names()
device_id = None


helloIntent = ["hi","hello","hey","hi there","hello there","hey there"]
exitIntent = ["exit","bye"]
timeIntent = ["time","tell me time","what's the time","time please"]
dateIntent = ["date","tell me date","what's the date","date please"]
shoesIntent = ["shoes","show me shoes","new shoes","branded shoes"]
phoneIntent = ["phones","mobile phones","smart phones","android phones","phone"]
Allnews = ["politics","india","education","sports","technology","world","lifestyle","entertainment"]



while True:
    #user_msg = input("Enter your message : ")

    for i, microphone_name in enumerate(mic_list):
        if microphone_name == mic_name:
            device_id = i

    with sr.Microphone(device_index = device_id, sample_rate = sample_rate,
                            chunk_size = chunk_size) as source:

        r.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = r.listen(source)
        print("Waiting for connection")
        text = r.recognize_google(audio)
        text = text.lower()
        print("you said: " + text)

        if text in helloIntent:
            print("Hey",name)


        elif text in timeIntent:
            curr_time = datetime.now().time()
            print("Time is",curr_time.strftime("%H:%M:%S,%p"))


        elif text in dateIntent:
            curr_date = datetime.now().date()
            print("Date is",curr_date.strftime("%d/%m/%y,%a"))


        elif text in shoesIntent:
            path="https://www.flipkart.com/search?q=shoes&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
            response=url.urlopen(path)
            page=bs4.BeautifulSoup(response,'lxml')
            title=page.find_all('div',class_='_2B_pmu')
            price=page.find_all('div',class_="_1vC4OE")

            for i in range(len(title)):
                print(title[i].text)
                print(price[i].text)

        elif text in phoneIntent:
            path="https://www.flipkart.com/search?q=smart+phones&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_0_5_na_na_na&otracker1=AS_Query_HistoryAutoSuggest_0_5_na_na_na&as-pos=0&as-type=HISTORY&suggestionId=smart+phones&requestId=e31d3850-478c-47a4-8e7d-1d05d1579c48&as-searchtext=smart"
            response=url.urlopen(path)
            page=bs4.BeautifulSoup(response,'lxml') 
            title=page.findAll('div',class_="_3wU53n")
            price=page.findAll('div',class_="_1vC4OE _2rQ-NK")

            for i in range(len(title)):
                print(title[i].text)
                print(price[i].text)
                print("="*60)

        elif text in exitIntent:
            print("See you soon",name)
            break

        elif text in Allnews:

            #newsname = input("Enter the news you want to see : ")
            path="https://www.indiatvnews.com/"+text
            response=url.urlopen(path)
            page=bs4.BeautifulSoup(response,'lxml')
            title=page.findAll('p',class_="titel")
    
            for i in range(len(title)):
                print(title[i].text)
                print("="*60)
            
        else:
            print("I don't recognize it what you have entered",name)

