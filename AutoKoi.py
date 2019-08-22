import pyautogui
import threading
#獲取螢幕大小
#get the size of your screen
width, height = pyautogui.size()
print("width is ", width, ", and height is", height)
#滑鼠指到目標處，獲取目標處位址
#point the mouse to the target, and get the position of the target
target = pyautogui.position()


def AutoClick():
#設定每次按按鍵中間間隔
#set the pause time between every click
    pyautogui.PAUSE = 20
    pyautogui.FAILSAFE = True

#在函式中重複呼叫，重複按4組
#use resursive function to repeat calling the function
    for i in range(5):
        for j in range(4):
            pyautogui.click(target)
    global timer
    timer = threading.Timer(3000, AutoClick)
    timer.start()

#第一次可以設定什麼時候開始
#set when will the first click
timer = threading.Timer(1, AutoClick)
timer.start()
