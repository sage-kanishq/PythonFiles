from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import concurrent.futures
opt = Options()
opt.set_headless()
assert opt.headless
driver = wd.Firefox(executable_path=GeckoDriverManager().install(),options=opt)
def playSong():
    def songs(song):
        song = song.lower()
        song = song.split(" ")
        if "loop" in song:                
            song.remove("loop")
            song = "+".join(song)
            driver.get("https://music.youtube.com/")
            
            driver.implicitly_wait(5)
            driver
            element = driver.find_element_by_css_selector("ytmusic-shelf-renderer.style-scope:nth-child(2) > div:nth-child(3) > ytmusic-responsive-list-item-renderer:nth-child(1) > div:nth-child(2) > ytmusic-thumbnail-renderer:nth-child(1)")
            hover = ActionChains(driver).move_to_element(element)
            hover.perform()
            driver.find_element_by_id("play-button").click()
            element = driver.find_element_by_css_selector("paper-icon-button.repeat:nth-child(2) > iron-icon:nth-child(1) > svg:nth-child(1) > g:nth-child(1) > path:nth-child(1)")
            doubleclk = ActionChains(driver).double_click(element)
            doubleclk.perform()

        else:
            song = "+".join(song)
            driver.get(f"https://music.youtube.com/")
            driver.implicitly_wait(5)
            driver.find_element_by_class_name("search-icon").click()
            driver.find_element_by_id("input").send_keys(song,Keys.ENTER)
            driver.find_element_by_css_selector("ytmusic-chip-cloud-chip-renderer.style-scope:nth-child(3) > a:nth-child(1) > yt-formatted-string:nth-child(3)").click()
            element = driver.find_element_by_id("content")
            hover = ActionChains(driver).move_to_element(element)
            hover.perform()
            driver.find_element_by_id("play-button").click()
    songs(input("Name of the song: "))
    while True:
        try:
            stop = input("Input :")
            stop=stop.lower()
            if stop=="jarvis quit" or stop == "jarvis break" or stop=="jarvis stop":
                driver.close()
                break
            elif stop=="jarvis play next" or stop=="jarvis play next song":
                driver.find_element_by_class_name("next-button").click()
            elif stop =="jarvis play previous" or stop=="jarvis play previous song":
                driver.find_element_by_class_name("previous-button").click()
            elif stop=="jarvis pause" or stop=="jarvis continue":
                driver.find_element_by_id("play-pause-button").click()

            elif stop=="jarvis skip advertisement":
                driver.find_element_by_id("ad-text:d").click()

            elif stop=="jarvis change song":
                a = input("Which song do you wanna hear :")
                songs(a)

        except Exception as e:
            print(f"Mmm I think the problem is that {e}")
                
playSong()
