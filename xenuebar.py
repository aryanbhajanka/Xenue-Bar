import os
from functools import wraps
import tkinter as tk
from tkinter import *
from ctypes import windll
from PIL import Image,ImageTk
import pyautogui
from time import strftime
import datetime
import webbrowser
from tkcalendar import Calendar
import psutil
import threading
import win32api, win32con, win32gui, win32process
from win32con import VK_MEDIA_PLAY_PAUSE, KEYEVENTF_EXTENDEDKEY
from winreg import *
import sqlite3
import time
 
conn = sqlite3.connect('database.db')
c = conn.cursor()
 
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS theme (colour TEXT)')

 
create_table()


c.execute("SELECT * FROM theme")
theme = rows = c.fetchall()

print(theme[0][0])

light_bg = ('#ecf4fc')
light_fg = ('black')
light_icon = ''

dark_bg = ('#182427')
dark_fg = ('white')
dark_icon = ''

if(theme[0][0]=='b'):
    bg = dark_bg
    fg = dark_fg
    icon = dark_icon
    alpha = 0.9
    sp_alpha = 0.9

elif(theme[0][0]=='w'):
    bg = light_bg
    fg = light_fg
    alpha = 0.85
    icon = light_icon
    sp_alpha = 0.7


def spotify():
    try:
        sp = tk.Toplevel()
        sp.geometry("916x35+480+0")
        sp.attributes('-alpha',sp_alpha)
        sp.configure(background=bg)
        windll.shcore.SetProcessDpiAwareness(1)
        sp.overrideredirect(True)
        sp.attributes('-topmost',True)
        #noice
        x = 1
        
        def quitapp():
            sp.destroy()

        def prev():
            pyautogui.press('prevtrack')

        def pause():
            pyautogui.press('playpause')

        def next():
            pyautogui.press('nexttrack')

        def mute():
            pyautogui.press('volumemute')

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

        song = Label(sp, text='', bg=bg, fg=fg, font = ('calibri', 10, 'bold'), border=0, highlightthickness=0,justify=CENTER, relief='sunken')    
        song.place(anchor='center', relx=0.47, rely=0.49)
        Button(sp,text="Close",command=quitapp, bg=bg, fg=fg,borderwidth=0, highlightthickness=0).place(relx=0.055, rely=0.495, anchor='e')
        Button(sp, text='🔇', bg=bg, fg=fg,borderwidth=0, highlightthickness=0, command=mute, font=('', 13)).place(relx=1, rely=0.495, anchor='e')
        Button(sp, text='⏮', bg=bg, fg=fg,borderwidth=0, highlightthickness=0, command=prev, font=('', 10)).place(relx=0.87999, rely=0.495, anchor='e')
        Button(sp, text='⏯️', bg=bg, fg=fg,borderwidth=0, highlightthickness=0, command=pause, font=('', 10)).place(relx=0.91599, rely=0.495, anchor='e')
        Button(sp, text='⏭️', bg=bg, fg=fg,borderwidth=0, highlightthickness=0, command=next, font=('', 10)).place(relx=0.95399, rely=0.495, anchor='e')


        def update():
            hp = Helper()
            info = hp.getInfo()
            if(info == 'Spotify Premium'):
                song.place_configure(relx=0.47)
                song.config(text='Your Spotify Player Is Idle')
            elif(info == ''):
                song.place_configure(relx=0.47)
                song.config(text='Your Spotify Player Is Idle') 
            elif(info == 'Spotify Free'):
                song.place_configure(relx=0.47)
                song.config(text='Your Spotify Player Is Idle')
            else: 
                if (len(info)>45):
                    song.place_configure(relx=0.47)
                    song.config(text=info[0:45]+'...')
                else:
                    song.config(text=info)
    
        def func2():
            while 0==0:
                update()
        
        t = threading.Thread(target=func2)
        t.start()

    except tk.TclError:
        pass
    
          
def calendar():
    Window = tk.Toplevel()
    Window.geometry("400x280+1500+35")
    Window.attributes('-alpha',0.95)
    Window.configure(background=bg)
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
                day = int(today.strftime("%d")))
    cal.config(background = bg, disabledbackground = bg , bordercolor = bg , headersbackground = bg , normalbackground = bg, foreground = fg, headersforeground = fg, disabledselectbackground = bg, weekendbackground = bg, weekendforeground = fg, othermonthbackground = bg, othermonthweforeground = 'grey', disableddaybackground = bg, tooltipbackground = bg, othermonthwebackground = bg, disabledforeground = fg, selectforeground = bg, disabledselectforeground = fg, disableddayforeground = fg, tooltipforeground = fg, normalforeground = fg, selectbackground = fg, showweeknumbers = False, showothermonthdays = False, font = ('', 10))
    cal.place(relx=0.48, rely=0.999, anchor='s') 


def power():
    app_power = tk.Toplevel()
    app_power.geometry("250x190+50+35")
    app_power.attributes('-alpha',0.95)
    app_power.configure(background=bg)
    windll.shcore.SetProcessDpiAwareness(1)
    app_power.overrideredirect(True)

    def quit():
        app_power.destroy()

    def shutdown():
        os.system("shutdown /s /t 1")

    def restart():
        os.system("shutdown /r /t 1")

    def lock():
        os.system("Rundll32.exe user32.dll,LockWorkStation")
 
    def quitapp():
        conn.close()
        menu.destroy()

    def change_theme():

        if(theme[0][0]=='b'):
            colour = 'w'
        elif(theme[0][0]=='w'):
            colour = 'b'

        c.execute('DELETE FROM theme')
        c.execute("INSERT INTO theme (colour) VALUES(?)", (colour))
        conn.commit()
        pop = tk.Toplevel()
        pop.geometry("600x80+300+145")
        pop.attributes('-alpha',0.95)
        pop.configure(background=bg)
        pop.attributes('-topmost',True)
        windll.shcore.SetProcessDpiAwareness(1)
        pop.overrideredirect(True)

        def quitpop():
            pop.destroy()

        Label(pop, text="Successful! Theme will be applied the next time you open Xenue Bar", fg=fg, bg=bg).pack()
        Button(pop,text="Ok",command=quitpop, height=1, width=3, bg=fg, borderwidth=0, fg=bg,highlightthickness=0).pack()



    Button(app_power,text="x",command=quit, height=1, width=3, bg='red', borderwidth=0, highlightthickness=0).place(relx=0.999, rely=0.09, anchor='e')
    Button(app_power, text="Shutdown", command=shutdown, bg=bg, fg=fg, borderwidth=0, highlightthickness=0).pack()
    Button(app_power, text="Restart", command=restart, bg=bg, fg=fg, borderwidth=0, highlightthickness=0).pack()
    Button(app_power, text="Lock", command=lock, bg=bg, fg=fg, borderwidth=0, highlightthickness=0).pack()
    Button(app_power, text="Quit Xenue Bar", command=quitapp, bg=bg, fg=fg, borderwidth=0, highlightthickness=0).pack()
    Button(app_power, text="Change Theme", command=change_theme, bg=bg, fg=fg, borderwidth=0, highlightthickness=0).pack()



def apps():    
    app_list = tk.Toplevel()
    app_list.geometry("380x450+50+35")
    app_list.attributes('-alpha',0.95)
    app_list.configure(background=bg)
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
    Label(app_list, text='Task View (Memory %):', bg=bg, fg=fg).place(relx=0.01, rely=0.05, anchor='w')
    Label(app_list,text='', bg=bg).pack()
    Label(app_list,text='', bg=bg).pack()
    scrollbarx = Scrollbar(app_list, orient='horizontal')
    scrollbarx.pack( side = BOTTOM, fill = X )
    scrollbar = Scrollbar(app_list, orient='vertical')
    scrollbar.pack( side = RIGHT, fill = Y )
    list = Listbox(app_list, yscrollcommand = scrollbar.set, width=300, height=400,xscrollcommand = scrollbarx.set, bg=bg, fg=fg, borderwidth=0, highlightthickness=0)
    for proc in psutil.process_iter():
        try:
            processName = proc.name()
            processID = round(proc.memory_percent())
        
            list.insert(END, (processName, processID,'%'))
            
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    list.pack(side = LEFT, fill = BOTH)
    scrollbarx.config( command = list.xview )
    scrollbar.config( command = list.yview )
    

global menu
menu = tk.Tk()

light_icon = (PhotoImage(file = 'light_icon.png'))
dark_icon = (PhotoImage(file = 'logo.png'))
light_logo = ('light_icon.png')
dark_logo = ('logo.png')

if(theme[0][0]=='b'):
    icon = dark_icon
    logo = dark_logo


elif(theme[0][0]=='w'):
    icon = light_icon
    logo = light_logo

windll.shcore.SetProcessDpiAwareness(1)
menu.overrideredirect(True)
menu.geometry("1950x35+0+0")
menu.attributes('-alpha',alpha)
menu.configure(background=bg)
menu.iconphoto(False, icon)

def windows():
    pyautogui.press('win')

def settings():
    with pyautogui.hold('win'):
        pyautogui.press('i')

def find():
    with pyautogui.hold('win'):
        pyautogui.press('s')

def times():
    string = strftime('%I:%M %p')
    lbl.config(text = string)
    lbl.after(1000, times)

def files():
    with pyautogui.hold('win'):
        pyautogui.press('e')

def actions():
    with pyautogui.hold('win'):
        pyautogui.press('a')

lbl = Button(menu, font = ('calibri', 10, 'bold'), bg=bg, fg=fg, command=lambda: calendar(), borderwidth=0, highlightthickness=0)
lbl.place(relx = 0.984, rely = 0.45, anchor = 'e')
times()

x = datetime.datetime.now()
day = Button(menu, text=x.strftime("%A") , bg=bg, font = ('calibri', 10, 'bold'), fg=fg, borderwidth=0, highlightthickness=0,command=lambda: calendar())
day.place(relx = 0.914, rely = 0.45, anchor = 'center')

image = Image.open(logo)
image = image.resize((28, 28), Image.ANTIALIAS)
my_img = ImageTk.PhotoImage(image)
Button(menu, text = '', image = my_img, command=windows, border=0, highlightthickness=0, borderwidth=0).place(relx = 0.008, rely = 0.485, anchor = 'w')
    
Button(menu, text='Ξ', highlightthickness=0, border=0, bg=bg, fg=fg, command=actions, font=("", 13)).place(relx = 0.885, rely = 0.53, anchor = 'e')

Button(menu, text = 'Power', bg=bg, fg=fg, border=0, command=power).place(relx = 0.031, rely = 0.48, anchor = 'w')
Button(menu, text='Find',bg=bg, fg=fg, border=0, command=find).place(relx = 0.0665, rely = 0.48, anchor = 'w')
Button(menu, text = 'Task View', bg=bg, fg=fg, border=0, command=apps).place(relx = 0.095, rely = 0.48, anchor = 'w')
Button(menu, text = 'Files', bg=bg, fg=fg, border=0, command=files).place(relx = 0.144, rely = 0.48, anchor = 'w')
Button(menu, text = 'Settings', bg=bg, fg=fg, border=0, command=settings).place(relx = 0.171, rely = 0.48, anchor = 'w')
Button(menu, text = 'Music', bg=bg, fg=fg, border=0, command=spotify).place(relx = 0.213, rely = 0.48, anchor = 'w')


def getlink(self):
    keyword = ''
    keyword = inputtxt.get(1.0, "end-1c")
    if (keyword==''):
        pass
    else:
        webbrowser.open('http://www.google.com/search?q='+keyword)
        inputtxt.delete(1.0, END)

global inputtxt
w = Canvas(menu, width=120, height=0, highlightthickness=0.5, highlightbackground=fg)
w.place(relx = 0.82, rely = 0.9, anchor = 's')
Label(menu, text="Quick Search:", bg=bg, fg=fg, border=0).place(relx = 0.725, rely = 0.48, anchor = 'w')
inputtxt = Text(menu, height=0, width=10, bg=bg, fg=fg, border=0, highlightthickness=0)
inputtxt.place(relx = 0.85, rely = 0.45, anchor = 'e')

menu.bind('<Return>', getlink)
menu.mainloop()
