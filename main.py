import pyautogui
import pandas as pd
from time import sleep

# System variables
URL = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
USER_EMAIL = 'beto_test@email.com'
USER_PASSW = 'SuP3Rs3cre7'

# Cursor / Mouse Pointer, depends on machine
# EMAIL_COORD = Point(x=1472, y=1515)
# PRODUCT_COORD = Point(x=2575, y=1201)

# Set fail-safe mode, moving mouse to the upper-left will abort program
pyautogui.FAILSAFE = True

# Set pause value, in seconds, between PyAutoGUI commands
pyautogui.PAUSE = 0.5

# Open system website
pyautogui.hotkey('win', 'f3')  # Personal custom shortcut for firefox
pyautogui.hotkey('win', 'up')  # Maximize window shortcut
pyautogui.typewrite(URL)
pyautogui.press('enter')

# Wait loading
sleep(3)

# Login
pyautogui.click(x=1472, y=1515)
pyautogui.typewrite(USER_EMAIL)
pyautogui.press('tab')
pyautogui.typewrite(USER_PASSW)
pyautogui.press('enter')

# Wait loading
sleep(3)

# Register product
