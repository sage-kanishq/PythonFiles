from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
options = webdriver.ChromeOptions()

options.add_argument("--user-data-dir=/home/kaushik/.config/google-chrome/Default")

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),options=options)
driver.get("youtube.com")