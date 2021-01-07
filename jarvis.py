import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import psutil
import time 
import pyjokes
import pyautogui
import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import urllib.request
import re
import lxml
from lxml import etree
import simplejson
import requests 
from requests_html import HTMLSession
#from googlesearch import search 
today = datetime.datetime.now()
engine = pyttsx3.init()
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 200)  
def speak(text):
    engine.say(text)
    engine.runAndWait()
cpu_per = psutil.cpu_percent(1)
battery = psutil.sensors_battery()

b_percent = str(battery.percent)
if(float(b_percent)<60.0):
    b_percent+="percent please plugin your charger"
else:
    b_percent+="percent no need to charge"
speak("welcome to casbergs personal assistent")
time.sleep(1)
speak("checking battery status")
time.sleep(1)
speak("battery remaining is"+b_percent)

def commands(sss):
    
    if("date" in sss):
        t_d = today
        
        speak("todays date is")
        #speak(t_d)
        time=datetime.datetime.now()
        speak(time.day)
        speak(time.strftime("%B"))
        speak(x.year)

        speak(x.strftime("%A"))
    elif("what you can do" in sss):
        speak("i can tell you todays date and i can search on wikipedia and search something on google and i can take screenshot and add  a note and also read it and  tell you a joke and play any song on youtube also recognising song name from its lyrics")
        speak("tell me what i have to do for you ")
        #takecommand().lower()
    elif("good" in sss):
        speak("thank you sir")
    elif("bored" in sss):
        speak("you can call your best friend or make some intresting things or use your whatsapp or instagram")
    elif("offline" in sss):
        speak("bye bye sir")
        exit(0)
    
    elif("search for" in sss):
        #wikipedia.set_lang("mr")
        sss = sss.replace("search for","")
        wiki_result = wikipedia.summary(sss, sentences = 2)
        speak(wiki_result)
    elif("open whatsapp" in sss):
        speak("opening whatsapp")
        webbrowser.open("web.whatsapp.com")
    elif("open" in sss):
        
        speak("opening in chrome browser")
        sss = sss.replace("open","")
        #sss = search(sss, tld="com", num=1, stop=2, pause=2)
        #b = webbrowser.get('chrome')
        sss = sss.replace(" ","")
        c = webbrowser.open("https://www.google.com/search?q="+sss)
        
        speak(c)
    
    elif("evaluate" in sss):
        speak("tell me first numbers ")
        
        comm1 = takecommand().lower()
        speak("tell me second number")
        comm2 = takecommand().lower()
        comm3 = int(comm1)+int(comm2)
        speak("addition of"+comm1+"plus"+comm2+"is"+str(comm3))
    elif("note" in sss):
        f = open("notes.txt","w")
        f.seek(0)
        speak("what to add")
        quer = takecommand().lower()
        speak("adding to notes")
        f.write(quer)
        
        speak("succfully took note")
        f.close()
    elif("read" in sss):
        f = open("notes.txt","r")
        speak(f.read())
        f.close()
    elif("joke" in sss):
        print(pyjokes.get_joke())
        speak(pyjokes.get_joke())
    elif("screenshot" in sss):
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(r'/home/casberg/Desktop/opencv/screen.png')
        speak("succesfully took screenshot")
    elif("news" in sss):
        news_url="https://news.google.com/news/rss"
        Client=urlopen(news_url)
        xml_page=Client.read()
        Client.close()

        soup_page=soup(xml_page,"lxml")
        news_list=soup_page.findAll("item")
# Print news title, url and publish date
        for news in range(0,5):
            print(news_list[news].title.text)
            speak(news_list[news].title.text)
    elif("youtube" in sss):
        
        sss = sss.replace("youtube","")
        sss = sss.replace(" ","+")
        html = urllib.request.urlopen("https://www.youtube.com/results?search_query="+sss)
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        #print(video_ids)
        url = "http://www.youtube.com/watch?v="+video_ids[0]
        r = requests.get(url) 
        #f = open("raw.txt","w")
        # converting the text 
        s = soup(r.text, "html.parser") 
        #print(s)
        # f.write(str(s))
        # f.close()
        # finding meta info for title 
        ss = str(s) 
        title = ss.find('videoDetails":{"videoId":')
        print(ss[title:title+1000])
        i = 48
        while True:
            if(ss[title+i]=='"'):
                break
            i+=1
        #f_title = ss[title:title+500].find('"title":')
        # ss = s[st_ind+14:st_ind+1000]
        # print(ss)
        # en_ind = ss.find('>')
        #print(ss[f_title:f_title+1000])
        #title = ss[st_ind:en_ind]
        #print(ss[title+48:title+i])
        speak("playing"+ss[title+48:title+i])
        speak("should i open the song in youtube")
        a = takecommand()
        if("ok" or "yes" or "sure" or "yupp" in sss):
            speak("opening in chrome ")
            webbrowser.open(url)
        else:
            speak("ok")
        # youtube = etree.HTML(urllib.urlopen(ans).read()) #enter your youtube url here
        # video_title = youtube.xpath("//span[@id='eow-title']/@title") #//get xpath using firepath firefox addon
        # print(''.join(video_title))
        # speak(video_title)
    else:
        speak(sss)

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("listning....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio,language='en-US')
        print(query)
        sss = query
        sss = query.lower()
        
        commands(sss)
        

    except Exception as e:
        print(e)
        return "None"
    return query

def talk():
    while True:
        takecommand()
        
talk()