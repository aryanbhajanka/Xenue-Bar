from functools import wraps
import tkinter as tk
from tkinter import *
from ctypes import alignment, windll
from typing import List
from PIL import Image,ImageTk
import pyautogui
import time
from time import strftime
import datetime
import webbrowser
from tkcalendar import Calendar
from ctypes import wintypes
import psutil
import os
import win32api, win32con, win32gui, win32process
from win32con import VK_MEDIA_PLAY_PAUSE, KEYEVENTF_EXTENDEDKEY

def spotify():
    sp = tk.Toplevel()
    sp.geometry("930x35+480+0")
    sp.attributes('-alpha',0.9)
    sp.configure(background='#182427')
    canvas = tk.Canvas(sp, height=150, width=400)
    windll.shcore.SetProcessDpiAwareness(1)
    sp.overrideredirect(True)
    sp.attributes('-topmost',True)
    
    class Helper():
        play_pause = 0xB3
        next_track = 0xB0
        previous_track = 0xB1
            
        def __init__(self):
            self.hwnd = 0

        def winEnumHandler(self, hwnd, ctx ):
            process_name = psutil.Process(win32process.GetWindowThreadProcessId(hwnd)[-1]).name()
            window_name = win32gui.GetWindowText(hwnd)
            if win32gui.IsWindowVisible(hwnd) and process_name == "Spotify.exe" and window_name != "":
                self.hwnd = hwnd

        def sendKey(self, key):
            win32api.keybd_event(key, 0, 0, 0)
            win32api.keybd_event(key, 0, win32con.KEYEVENTF_KEYUP, 0)

        def getInfo(self):
            win32gui.EnumWindows(self.winEnumHandler, None)
            return win32gui.GetWindowText(self.hwnd)

    def quitapp():
        sp.destroy()

    hp = Helper()
    info = hp.getInfo()
    long_song = Label(sp, text=info[0:45]+'...', bg='#182427', fg='white', font = ('calibri', 10, 'bold'))
    song = Label(sp, text=info, bg='#182427', fg='white', font = ('calibri', 10, 'bold'))
    idle = Label(sp, text='Your Spotify Player Is Idle', bg='#182427', fg='white', font = ('calibri', 10, 'bold'))
    Button(sp,text="Close",command=quitapp, bg='#182427', fg='white',borderwidth=0, highlightthickness=0).place(relx=0.05, rely=0.495, anchor='e')
    Button(sp, text='||◁', bg='#182427', fg='white',borderwidth=0, highlightthickness=0).place(relx=0.89, rely=0.495, anchor='e')
    Button(sp, text='| |', bg='#182427', fg='white',borderwidth=0, highlightthickness=0).place(relx=0.926, rely=0.495, anchor='e')
    Button(sp, text='▷||', bg='#182427', fg='white',borderwidth=0, highlightthickness=0).place(relx=0.97, rely=0.495, anchor='e')

    if(info == 'Spotify Premium'):
        idle.place(anchor='e', relx=0.6, rely=0.49)
    elif(info == ''):
        idle.place(anchor='e', relx=0.6, rely=0.49)
    else: 
        if (len(info)>45):
            long_song.place(anchor='e', relx=0.6, rely=0.49)
        else:
           song.place(anchor='e', relx=0.6, rely=0.49)

   
                   

def calendar():
    Window = tk.Toplevel()
    Window.geometry("400x300+1500+35")
    Window.attributes('-alpha',0.95)
    Window.configure(background='#182427')
    canvas = tk.Canvas(Window, height=150, width=400)
    windll.shcore.SetProcessDpiAwareness(1)
    Window.overrideredirect(True)
    from datetime import date
    today = date.today()

    def quit():
        Window.destroy()

    Button(Window,text="x",command=quit, height=1, width=3, bg='red', borderwidth=0, highlightthickness=0).place(relx=0.999, rely=0.05, anchor='e')
    cal = Calendar(Window, selectmode = 'day',
                year = int(today.strftime("%y")), month = int(today.strftime("%m")),
                day = int(today.strftime("%d")), )
    
    cal.place(relx=0.48, rely=0.93, anchor='s') 

def power():
    app_power = tk.Toplevel()
    app_power.geometry("250x250+50+35")
    app_power.attributes('-alpha',0.95)
    app_power.configure(background='#182427')
    windll.shcore.SetProcessDpiAwareness(1)
    app_power.overrideredirect(True)

    def quit():
        app_power.destroy()

    def shutdown():
        os.system("shutdown /s /t 1")

    def restart():
        os.system("restart /s /t 1")

    def sleep():
        os.system("sleep /s /t 1")
 
    def quitapp():
        menu.destroy()

    Button(app_power,text="x",command=quit, height=1, width=3, bg='red', borderwidth=0, highlightthickness=0).place(relx=0.999, rely=0.05, anchor='e')
    Button(app_power, text="Shutdown", command=shutdown, bg='#182427', fg='white', borderwidth=0, highlightthickness=0).pack()
    Button(app_power, text="Restart", command=restart, bg='#182427', fg='white', borderwidth=0, highlightthickness=0).pack()
    Button(app_power, text="Sleep", command=sleep, bg='#182427', fg='white', borderwidth=0, highlightthickness=0).pack()
    Button(app_power, text="Quit Xienu Bar", command=quitapp, bg='#182427', fg='white', borderwidth=0, highlightthickness=0).pack()


def apps():    
    app_list = tk.Toplevel()
    app_list.geometry("380x450+50+35")
    app_list.attributes('-alpha',0.95)
    app_list.configure(background='#182427')
    windll.shcore.SetProcessDpiAwareness(1)
    app_list.overrideredirect(True)

    def quit():
        app_list.destroy()

    def task_view():
        with pyautogui.hold('ctrl'):
            with pyautogui.hold('shift'):
                pyautogui.press('esc')
    
    Button(app_list,text="x",command=quit, height=1, width=3, bg='red', borderwidth=0, highlightthickness=0).place(relx=0.999, rely=0.05, anchor='e')
    Button(app_list,text="Manage",command=task_view, height=1, width=7, bg='grey', borderwidth=0, highlightthickness=0).place(relx=0.9, rely=0.05, anchor='e')
    Label(app_list, text='Task View:', bg='#182427', fg='white').place(relx=0.01, rely=0.05, anchor='w')
    Label(app_list,text='', bg='#182427').pack()
    Label(app_list,text='', bg='#182427').pack()
    scrollbarx = Scrollbar(app_list, orient='horizontal')
    scrollbarx.pack( side = BOTTOM, fill = X )
    scrollbar = Scrollbar(app_list, orient='vertical')
    scrollbar.pack( side = RIGHT, fill = Y )
    list = Listbox(app_list, yscrollcommand = scrollbar.set, width=300, height=400,xscrollcommand = scrollbarx.set, bg='#182427', fg='white', borderwidth=0, highlightthickness=0)
    for proc in psutil.process_iter():
        try:
            processName = proc.name()
            processID = proc.cpu_percent()
        
            list.insert(END, (processName, processID,'%'))
            
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    list.pack(side = LEFT, fill = BOTH)
    scrollbarx.config( command = list.xview )
    scrollbar.config( command = list.yview )
    
    

menu = tk.Tk()

windll.shcore.SetProcessDpiAwareness(1)
menu.overrideredirect(True)
menu.geometry("1950x35+0+0")
menu.attributes('-alpha',0.95)
menu.configure(background='#182427')

def windows():
    pyautogui.press('win')

def settings():
    with pyautogui.hold('win'):
        pyautogui.press('i')

def find():
    with pyautogui.hold('win'):
        pyautogui.press('s')

def times():
    string = strftime('%H:%M %p')
    lbl.config(text = string)
    lbl.after(1000, times)

def files():
    with pyautogui.hold('win'):
        pyautogui.press('e')

lbl = Button(menu, font = ('calibri', 10, 'bold'), bg='#182427', fg='white', command=lambda: calendar(), borderwidth=0, highlightthickness=0)
lbl.place(relx = 0.982, rely = 0.45, anchor = 'e')
times()

x = datetime.datetime.now()
day = Button(menu, text=x.strftime("%A") ,font = ('calibri', 10, 'bold'), bg='#182427', fg='white', borderwidth=0, highlightthickness=0,command=lambda: calendar())
day.place(relx = 0.934, rely = 0.45, anchor = 'e')

image = Image.open('logo.png')
image = image.resize((33, 33), Image.ANTIALIAS)
my_img = ImageTk.PhotoImage(image)
Button(menu, text = '', image = my_img, command=windows, border=0, highlightthickness=0).place(relx = 0.005, rely = 0.48, anchor = 'w')


Button(menu, text = 'Power', bg='#182427', fg='white', border=0, command=power).place(relx = 0.035, rely = 0.48, anchor = 'w')
Button(menu, text='Find',bg='#182427', fg='white', border=0, command=find).place(relx = 0.07, rely = 0.48, anchor = 'w')
Button(menu, text = 'Task View', bg='#182427', fg='white', border=0, command=apps).place(relx = 0.097, rely = 0.48, anchor = 'w')
Button(menu, text = 'Files', bg='#182427', fg='white', border=0, command=files).place(relx = 0.144, rely = 0.48, anchor = 'w')
Button(menu, text = 'Settings', bg='#182427', fg='white', border=0, command=settings).place(relx = 0.169, rely = 0.48, anchor = 'w')
Button(menu, text = 'Music', bg='#182427', fg='white', border=0, command=spotify).place(relx = 0.21, rely = 0.48, anchor = 'w')


def getlink(self):
    keyword = ''
    keyword = inputtxt.get(1.0, "end-1c")
    webbrowser.open('http://www.google.com/search?q='+keyword)
    inputtxt.delete(1.0, END)

global inputtxt
w = Canvas(menu, width=120, height=0, highlightthickness=0.5)
w.place(relx = 0.83, rely = 0.9, anchor = 's')
Label(menu, text="Quick Search:", bg='#182427', fg='white', border=0).place(relx = 0.735, rely = 0.48, anchor = 'w')
inputtxt = Text(menu, height=0, width=10, bg='#182427', fg='white', border=0, highlightthickness=0)
inputtxt.place(relx = 0.86, rely = 0.45, anchor = 'e')
menu.bind('<Return>', getlink)

menu.mainloop()
