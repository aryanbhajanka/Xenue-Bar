#Run this file before running xenuebar.py to install the required packages

import os
import time

print("Installing pakages for Xenue Bar by Aryan Bhajanka...")
print("https://github.com/aryanbhajanka/Xenue-Bar.git")
time.sleep(2)

os.system('pip install functools')
os.system('pip install pywin32')
os.system('pip install psutil')
os.system('pip install tkcalendar')
os.system('pip install datetime')
os.system('pip install pyautogui')

print("Installation Complete\n")
time.sleep(2)
print("Thank You for using Xenue Bar")
print("You can now run xenuebar.py to access Xenue Bar")
time.sleep(5)
quit()
