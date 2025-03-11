import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
options=Options()
options.add_argument('user-data-dir=/Users/monyatwu/selenium_profiles')
options.add_argument('profile-directory=Default')

driver=webdriver.Chrome(service=Service(),options=options)
driver.get("https://www.youtube.com/playlist?list=PLV8YnLyeUO1cng0dftZXQkwyY_DkJ8Xcj")
input("press enter to close browser")
driver.quit()
