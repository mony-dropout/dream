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
time.sleep(20)
print("went to website")
three_dots=driver.find_element(By.XPATH,'//*[@id="page-header"]/yt-page-header-renderer/yt-page-header-view-model/div[2]/div[2]/yt-flexible-actions-view-model/div/div[4]/button-view-model/button/yt-touch-feedback-shape/div/div[2]')
three_dots.click()
time.sleep(2)
print("three dots clicked")
shuffle_button=driver.find_element(By.XPATH,'//*[@id="contentWrapper"]/yt-sheet-view-model/yt-contextual-sheet-layout/div[2]/yt-list-view-model/yt-list-item-view-model[1]/div/div[2]/div/span')
shuffle_button.click()
time.sleep(10)
print("shuffle button clicked")
next_button=driver.find_element(By.XPATH,'//*[@id="movie_player"]/div[28]/div[2]/div[1]/a[2]')
next_button.click()
time.sleep(10)
next_button=driver.find_element(By.XPATH,'//*[@id="movie_player"]/div[28]/div[2]/div[1]/a[2]')
next_button.click()
time.sleep(10)
next_button=driver.find_element(By.XPATH,'//*[@id="movie_player"]/div[28]/div[2]/div[1]/a[2]')
next_button.click()
time.sleep(10)
driver.quit()
