from apscheduler.schedulers.blocking import BlockingScheduler
import pyautogui
import time
import random

now=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
target = pyautogui.position()
print(now)

def AutoClick():
#設定每次按按鍵中間間隔，單位為秒
#set the pause time between every click
#ver2.1 新增以亂數秒點擊
    pyautogui.PAUSE = random.randint(20,30)
    pyautogui.FAILSAFE = True

#在函式中重複呼叫，重複按4組
#use resursive function to repeat calling the function
    for i in range(5):
        for j in range(4):
            pyautogui.click(target)

AutoClick()
sched = BlockingScheduler()
sched.add_job(AutoClick, 'interval', minutes=50)

sched.start()
