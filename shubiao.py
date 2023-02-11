#!/usr/bin/env python
#!-*-coding:utf-8 -*-
#import time
#import random
#import pyautogui
 
#while 1:
    # 5秒钟移动一次鼠标(移动鼠标时间可以根据自己需要设定)
    #time.sleep(5)
    #pyautogui.moveTo(x=1500,y=random.randint(100,900))
from pymouse import PyMouse
from win32api import GetSystemMetrics
import random
import time
import pyautogui as gui



m = PyMouse()
m.position()

width = GetSystemMetrics(0)
heigth = GetSystemMetrics(1)

m.move(100, 100)
while True:
 x = random.randint(0, width)
 y = random.randint(0, heigth)
 m.move(x, y)
 def click_position(x,y,buttonkey='left'):#模拟点击（默认左键）
    gui.click(x,y,button=buttonkey)
    gui.press("CapsLock")
    #gui.typewrite("moyu")
 #gui.click(x,y,button=buttonkey)
 time.sleep(random.randint(3, 5))