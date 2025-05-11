import pydirectinput
import time
import pyautogui

# 關閉 fail-safe
pydirectinput.FAILSAFE = False

def A(x):
    start_time = time.time()
    while True:
        pydirectinput.keyDown('q')
        if time.time() - start_time >= x:
            pydirectinput.keyUp('q')
            break
def Buff():
    for key in ['9', '8', '7']:#buff 倫 賣裝
        pydirectinput.press(key)
        time.sleep(2)

# 初始 Buff 一次
Buff()
pydirectinput.press('=')
a = 0
while True:
    while a != 15:    
        A(60)
        a += 1
        print(a)
    if a == 15:
        A(60)
        Buff()
        pydirectinput.press('=')
        a = 0
