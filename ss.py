import pyautogui
import time
def screenshot(s):
   time.sleep(5)
   screenshot = pyautogui.screenshot()
   screenshot.save(s+".png")
