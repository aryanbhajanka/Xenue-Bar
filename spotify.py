import win32api, win32con, win32gui, win32process
from win32con import VK_MEDIA_PLAY_PAUSE, KEYEVENTF_EXTENDEDKEY
import psutil

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




        