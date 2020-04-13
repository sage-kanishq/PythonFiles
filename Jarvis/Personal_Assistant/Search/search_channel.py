from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.action_chains import ActionChains
def search_app(channel=input("Which Channel do you want to view :")):
    driver = wd.Firefox(executable_path=GeckoDriverManager().install())
    # driver.set_page_load_timeout(15)
    driver.get("https://www.youtube.com/")
    search_ele = driver.find_element_by_name("search_query")
    search_ele.send_keys(channel,Keys.ENTER)



if __name__=="__main__":
    channel =input("Which Channel do you want to view : ")
    search_app(channel)
    
