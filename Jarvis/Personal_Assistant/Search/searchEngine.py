from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.action_chains import ActionChains
def searchQuestion(query):
    driver = wd.Firefox(executable_path=GeckoDriverManager().install())
    driver.get("https://duckduckgo.com/")
    driver.find_element_by_name("q").send_keys(query,Keys.ENTER)
    driver.find_element_by_id("r1-0").click()


if __name__=="__main__":
    searchQuestion(input("What shall I search for ? :"))
