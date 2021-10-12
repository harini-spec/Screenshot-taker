from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time 
import pandas as pd
import pyscreenshot as ImageGrab

PATH = "/home/harini/Downloads/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(PATH)

def screenshot(s):
   driver.get(s)
   driver.maximize_window()
   time.sleep(5)
   screenshot1 = ImageGrab.grab(bbox=(0, 0, 1920, 1080))
   screenshot1.save("demo.png")
