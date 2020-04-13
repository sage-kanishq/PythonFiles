print("Initializing...")
import os
import wikipedia
import datetime
from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import enchant
print("Opening Browser For Testing...")
driver = wd.Firefox(executable_path=GeckoDriverManager().install())
os.system("clear")
# driver.close()
opt = Options()
opt.set_headless()
assert opt
headless_driver = wd.Firefox(executable_path=GeckoDriverManager().install(),options=opt)
# headless_driver.close()
print("Looking Good. Clearing Terminal.")
os.system("clear")
dictionary = enchant.Dict("en_UK")

def search_app(channel=""):
    channel=input("Which Video do you want to view :")
    driver.get("https://www.youtube.com/")
    search_ele = driver.find_element_by_name("search_query")
    search_ele.send_keys(channel,Keys.ENTER)

def searchQuestion(query):
    driver.get("https://duckduckgo.com/")
    driver.find_element_by_name("q").send_keys(query,Keys.ENTER)

def wiki(query,lines=2):
    query = query.lower()
    print(wikipedia.summary(query))

def playSong():
    def songs(song):
        song = song.lower()
        song = song.split(" ")
        if "loop" in song:                
            song.remove("loop")
            song = "".join(song)
            headless_driver.get(f"https://music.youtube.com/search?q={song}")
            headless_driver.implicitly_wait(5)
            element = headless_driver.find_element_by_css_selector("ytmusic-shelf-renderer.style-scope:nth-child(2) > div:nth-child(3) > ytmusic-responsive-list-item-renderer:nth-child(1) > div:nth-child(2) > ytmusic-thumbnail-renderer:nth-child(1)")
            hover = ActionChains(headless_driver).move_to_element(element)
            hover.perform()
            headless_driver.find_element_by_id("play-button").click()
            element = headless_driver.find_element_by_css_selector("paper-icon-button.repeat:nth-child(2) > iron-icon:nth-child(1) > svg:nth-child(1) > g:nth-child(1) > path:nth-child(1)")
            doubleclk = ActionChains(headless_driver).double_click(element)
            doubleclk.perform()

        else:
            song = "".join(song)
            headless_driver.get(f"https://music.youtube.com/search?q={song}")
            headless_driver.implicitly_wait(5)
            element = headless_driver.find_element_by_css_selector("ytmusic-shelf-renderer.style-scope:nth-child(2) > div:nth-child(3) > ytmusic-responsive-list-item-renderer:nth-child(1) > div:nth-child(2) > ytmusic-thumbnail-renderer:nth-child(1)")
            hover = ActionChains(headless_driver).move_to_element(element)
            hover.perform()
            headless_driver.find_element_by_id("play-button").click()

    a = input("Name of the song: ")
    songs(a)

    while True:
        try:
            stop = input("Input :")
            stop=stop.lower()
            if stop=="jarvis quit" or stop == "jarvis break" or stop=="jarvis stop":
                headless_driver.get("https://duckduckgo.com/")
                break
            elif stop=="jarvis play next" or stop=="jarvis play next song":
                headless_driver.find_element_by_class_name("next-button").click()
            elif stop =="jarvis play previous" or stop=="jarvis play previous song":
                headless_driver.find_element_by_class_name("previous-button").click()
            elif stop=="jarvis pause" or stop=="jarvis continue":
                headless_driver.find_element_by_id("play-pause-button").click()

            elif stop=="jarvis skip advertisement":
                headless_driver.find_element_by_class_name("ytp-ad-skip-button-container").click()

            elif stop=="jarvis change song":
                a = input("Which song do you wanna hear :")
                songs(a)

        except Exception as e:
            print(f"Mmm I think the problem is that {e}")

def greet():
    hour = int(datetime.datetime.now().hour) 
    if 16>hour>12:
        print("Good Afternoon Sir")
        print("I am J.A.R.V.I.S your Personal Assistant.")

    elif 8<hour<12:
        print("Good Morning")
        print("I am J.A.R.V.I.S")
    elif 16<=hour<=21:
        print("Good Evening Sir.")    
        print("I am J.A.R.V.I.S your Personal Assistant.")

    else:
        print("I think you would be better, of with some sleep. Just suggesting!")
        print("By the way. I am J.A.R.V.I.S.")

def currentTime():
    a = str(datetime.datetime.now())
    a=a.split(".")
    a.pop()
    a="".join(a)
    fulldate,time = a.split(" ")
    year,month,date = fulldate.split("-") 
    print(f"Date :{date} Year :{year} Month :{month}")
    print(f"Time :{time}")
greet()
while True:
    try:
        s = input("Ask :")
        if "jarvis" not in s:
            continue
        s = s.replace("jarvis","")
        if "play" in s and "song" in s:
            playSong()

        elif "quit" in s:
            headless_driver.quit()
            driver.quit()
            print("Quiting Sir thank you for your time.")
            os.system("clear")
            break
        elif "close tab" in s or "stop" in s and "jarvis" in s:
            driver.get("https://duckduckgo.com/") 

        elif "time" in s or "date" in s:
            currentTime()

        elif "wikipedia" in s or "Wikipedia":
            s.replace("wikipedia","")
            wiki(s)

        elif "who are you":
            greet()

        else:
            print("Sorry!, Didn't Get You")

    except Exception as e:
        print(f"Mmmm I think the problem is {e}")
        continue