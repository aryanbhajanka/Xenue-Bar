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
import os
from spotify import Helper
import threading


def spotify():
    #def func1():
    sp = tk.Toplevel()
    sp.geometry("916x35+480+0")
    sp.attributes('-alpha',0.9)
    sp.configure(background='#182427')
    canvas = tk.Canvas(sp, height=150, width=400)
    windll.shcore.SetProcessDpiAwareness(1)
    sp.overrideredirect(True)
    sp.attributes('-topmost',True)
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

    c = Canvas(height=35, width=100)
    song = Label(sp, text='', bg='#182427', fg='white', font = ('calibri', 10, 'bold'), border=0, highlightthickness=0,justify=CENTER, relief='sunken')    
    song.place(anchor='center', relx=0.47, rely=0.49)
    #c.place()
    Button(sp,text="Close",command=quitapp, bg='#182427', fg='white',borderwidth=0, highlightthickness=0).place(relx=0.055, rely=0.495, anchor='e')
    Button(sp, text='🔇', bg='#182427', fg='white',borderwidth=0, highlightthickness=0, command=mute, font=('', 13)).place(relx=1, rely=0.495, anchor='e')
    Button(sp, text='⏮', bg='#182427', fg='white',borderwidth=0, highlightthickness=0, command=prev, font=('', 10)).place(relx=0.87999, rely=0.495, anchor='e')
    Button(sp, text='⏯️', bg='#182427', fg='white',borderwidth=0, highlightthickness=0, command=pause, font=('', 10)).place(relx=0.91599, rely=0.495, anchor='e')
    Button(sp, text='⏭️', bg='#182427', fg='white',borderwidth=0, highlightthickness=0, command=next, font=('', 10)).place(relx=0.95399, rely=0.495, anchor='e')


    def update():
        hp = Helper()
        info = hp.getInfo()
        if(info == 'Spotify Premium'):
            song.place_configure(relx=0.47)
            song.config(text='Your Spotify Player Is Idle')
        elif(info == ''):
            song.place_configure(relx=0.47)
            song.config(text='Your Spotify Player Is Idle') 
        else: 
            if (len(info)>45):
                song.place_configure(relx=0.47)
                song.config(text=info[0:45]+'...')
            else:
                song.config(text=info)
#20
    def func2():
        while 0==0:
            update()
    
    t = threading.Thread(target=func2)
    t.start()
    
          
def calendar():
    Window = tk.Toplevel()
    Window.geometry("400x280+1500+35")
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
                day = int(today.strftime("%d")))
    cal.config(background = '#182427', disabledbackground = "#182427" , bordercolor = "#182427" , headersbackground = "#182427" , normalbackground = "#182427", foreground = 'white', headersforeground = 'white', disabledselectbackground = '#182427', weekendbackground = '#182427', weekendforeground = 'white', othermonthbackground = '#182427', othermonthweforeground = 'grey', disableddaybackground = '#182427', tooltipbackground = '#182427', othermonthwebackground = '#182427', disabledforeground = 'white', selectforeground = 'black', disabledselectforeground = 'white', disableddayforeground = 'white', tooltipforeground = 'white', normalforeground = 'white', selectbackground = 'white', showweeknumbers = False, showothermonthdays = False, font = ('', 10))
    cal.place(relx=0.48, rely=0.999, anchor='s') 

def power():
    app_power = tk.Toplevel()
    app_power.geometry("250x170+50+35")
    app_power.attributes('-alpha',0.95)
    app_power.configure(background='#182427')
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
        menu.destroy()

    Button(app_power,text="x",command=quit, height=1, width=3, bg='red', borderwidth=0, highlightthickness=0).place(relx=0.999, rely=0.05, anchor='e')
    Button(app_power, text="Shutdown", command=shutdown, bg='#182427', fg='white', borderwidth=0, highlightthickness=0).pack()
    Button(app_power, text="Restart", command=restart, bg='#182427', fg='white', borderwidth=0, highlightthickness=0).pack()
    Button(app_power, text="Lock", command=lock, bg='#182427', fg='white', borderwidth=0, highlightthickness=0).pack()
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
    Label(app_list, text='Task View (Memory %):', bg='#182427', fg='white').place(relx=0.01, rely=0.05, anchor='w')
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
            processID = round(proc.memory_percent())
        
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
    string = strftime('%I:%M %p')
    lbl.config(text = string)
    lbl.after(1000, times)

def files():
    with pyautogui.hold('win'):
        pyautogui.press('e')

def actions():
    with pyautogui.hold('win'):
        pyautogui.press('a')

lbl = Button(menu, font = ('calibri', 10, 'bold'), bg='#182427', fg='white', command=lambda: calendar(), borderwidth=0, highlightthickness=0)
lbl.place(relx = 0.984, rely = 0.45, anchor = 'e')
times()

x = datetime.datetime.now()
day = Button(menu, text=x.strftime("%A") , bg='#182427', font = ('calibri', 10, 'bold'), fg='white', borderwidth=0, highlightthickness=0,command=lambda: calendar())
day.place(relx = 0.907, rely = 0.45, anchor = 'center')

image = Image.open('logo2.png')
image = image.resize((28, 28), Image.ANTIALIAS)
my_img = ImageTk.PhotoImage(image)
Button(menu, text = '', image = my_img, command=windows, border=0, highlightthickness=0, borderwidth=0).place(relx = 0.008, rely = 0.485, anchor = 'w')

Button(menu, text='☰', highlightthickness=0, border=0, bg='#182427', fg='white', command=actions, font=("", 11)).place(relx = 0.875, rely = 0.53, anchor = 'e')

Button(menu, text = 'Power', bg='#182427', fg='white', border=0, command=power).place(relx = 0.031, rely = 0.48, anchor = 'w')
Button(menu, text='Find',bg='#182427', fg='white', border=0, command=find).place(relx = 0.0665, rely = 0.48, anchor = 'w')
Button(menu, text = 'Task View', bg='#182427', fg='white', border=0, command=apps).place(relx = 0.095, rely = 0.48, anchor = 'w')
Button(menu, text = 'Files', bg='#182427', fg='white', border=0, command=files).place(relx = 0.144, rely = 0.48, anchor = 'w')
Button(menu, text = 'Settings', bg='#182427', fg='white', border=0, command=settings).place(relx = 0.171, rely = 0.48, anchor = 'w')
Button(menu, text = 'Music', bg='#182427', fg='white', border=0, command=spotify).place(relx = 0.213, rely = 0.48, anchor = 'w')


def getlink(self):
    keyword = ''
    keyword = inputtxt.get(1.0, "end-1c")
    if (keyword==''):
        pass
    else:
        webbrowser.open('http://www.google.com/search?q='+keyword)
        inputtxt.delete(1.0, END)

global inputtxt
w = Canvas(menu, width=120, height=0, highlightthickness=0.5)
w.place(relx = 0.82, rely = 0.9, anchor = 's')
Label(menu, text="Quick Search:", bg='#182427', fg='white', border=0).place(relx = 0.725, rely = 0.48, anchor = 'w')
inputtxt = Text(menu, height=0, width=10, bg='#182427', fg='white', border=0, highlightthickness=0)
inputtxt.place(relx = 0.85, rely = 0.45, anchor = 'e')

menu.bind('<Return>', getlink)

menu.mainloop()
