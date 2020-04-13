from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.action_chains import ActionChains
def search_in_prime(video=None):
    driver = wd.Firefox(executable_path=GeckoDriverManager().install())
    driver.get("https://www.primevideo.com/")
    driver.find_element_by_link_text("Sign In").click()
    driver.find_element_by_id("ap_email").send_keys("sarkar.kaushik.2000@gmail.com")
    driver.find_element_by_id("ap_password").send_keys("bangalore")
    driver.find_element_by_id("signInSubmit").click()