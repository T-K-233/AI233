# https://www.geeksforgeeks.org/mouse-keyboard-automation-using-python/

import time

import pyautogui


# myScreenshot = pyautogui.screenshot(region=(0,0, 300, 400))
# myScreenshot.save("view.png")




# import numpy as np
# import cv2
# from mss import mss
# from PIL import Image

# bounding_box = {'top': 100, 'left': 0, 'width': 400, 'height': 300}

# sct = mss()

# while True:
#     sct_img = sct.grab(bounding_box)
#     cv2.imshow('screen', np.array(sct_img))

#     if (cv2.waitKey(1) & 0xFF) == ord('q'):
#         cv2.destroyAllWindows()
#         break
#pyautogui.moveTo(100, 100, duration = 1)


import win32gui
import win32con


class WeChatDriver:
    def __init__(self):
        pass
    
    def getWindow(self):
        self.hwnd = win32gui.FindWindow(None, "Weixin")
        return self.hwnd
    
    def bringToFront(self):
        win32gui.ShowWindow(self.hwnd, win32con.SW_RESTORE)
        win32gui.SetWindowPos(self.hwnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)  
        win32gui.SetWindowPos(self.hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)  
        win32gui.SetWindowPos(self.hwnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_SHOWWINDOW + win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)

    def maximizeWindow(self):
        win32gui.ShowWindow(self.hwnd, win32con.SW_MAXIMIZE)

    def getWindowRect(self):
        rect = win32gui.GetWindowRect(self.hwnd)
        return rect

    def setWindowRect(self):
        rect = win32gui.GetWindowRect(self.hwnd)
        x0, y0, x1, y1 = rect
        w = x1 - x0 # width
        h = y1 - y0 # height
        win32gui.SetWindowPos(self.hwnd, win32con.HWND_TOPMOST, x0, y0, w+100, h+200, win32con.SWP_SHOWWINDOW)


def listAllWindows():
    def callback(hwnd, extra):
        rect = win32gui.GetWindowRect(hwnd)
        x = rect[0]
        y = rect[1]
        w = rect[2] - x
        h = rect[3] - y
        
        if win32gui.GetWindowText(hwnd) == "Weixin":
            print("Window %s:" % win32gui.GetWindowText(hwnd))
            print("\tLocation: (%d, %d)" % (x, y))
            print("\t    Size: (%d, %d)" % (w, h))
    win32gui.EnumWindows(callback, None)

    

wx = WeChatDriver()
wx.getWindow()
wx.bringToFront()
wx.maximizeWindow()
print(wx.getWindowRect())

time.sleep(0.1)
myScreenshot = pyautogui.screenshot(region=(0, 0, 2256, 1444))
myScreenshot.save("view.png")

#win32gui.MoveWindow(hwnd, x0, y0, w+100, h+200, True)
#SetWindowPos(hWnd, InsertAfter, X, Y, cx, cy, Flags)





