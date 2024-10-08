import pyautogui
import pandas as pd
from time import sleep

# System variables9.95  5.0 CAHA000251  Hashtag Camisa
URL = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
USER_EMAIL = 'beto_test@email.com'
USER_PASSW = 'SuP3Rs3cre7'
CSV_PATH = 'data/produtos_test.csv'

# Cursor / Mouse Pointer, depends on machine display
# EMAIL_COORD = Point(x=746, y=436)
# PRODUCT_COORD = Point(x=706, y=321)
# SEND_COORD = Point(x=872, y=967)

# Set fail-safe mode, moving mouse to the upper-left will abort program
pyautogui.FAILSAFE = True

# Set pause value, in seconds, between PyAutoGUI commands
pyautogui.PAUSE = 0.5

# Open system website
pyautogui.hotkey('win', 'f3')  # Personal custom shortcut for firefox
sleep(0.5)
pyautogui.hotkey('win', 'up')  # Maximize window shortcut
sleep(0.5)
pyautogui.typewrite(URL)
pyautogui.press('enter')

# Wait loading
sleep(3)

# Login
pyautogui.click(x=746, y=436)
pyautogui.typewrite(USER_EMAIL)
pyautogui.press('tab')
pyautogui.typewrite(USER_PASSW)
pyautogui.press('enter')

# Wait loading
sleep(3)

# Import data from csv
table = pd.read_csv(CSV_PATH)

# Register products
for _ in table.index:
    pyautogui.click(x=706, y=321)
    pyautogui.typewrite(str(table.loc[_, 'codigo']))
    pyautogui.press('tab')
    pyautogui.typewrite(str(table.loc[_, 'marca']))
    pyautogui.press('tab')
    pyautogui.typewrite(str(table.loc[_, 'tipo']))
    pyautogui.press('tab')
    pyautogui.typewrite(str(table.loc[_, 'categoria']))
    pyautogui.press('tab')
    pyautogui.typewrite(str(table.loc[_, 'preco_unitario']))
    pyautogui.press('tab')
    pyautogui.typewrite(str(table.loc[_, 'custo']))
    pyautogui.press('tab')
    if not pd.isna(table.loc[_, 'obs']):
        pyautogui.typewrite(str(table.loc[_, 'obs']))
    pyautogui.click(x=872, y=967)
