from apscheduler.schedulers.blocking import BlockingScheduler
import pyautogui
import time
import random

now=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
target = pyautogui.position()
print(now)
target_pix = pyautogui.screenshot().getpixel((target))



def AutoClick():
#設定每次按按鍵中間間隔
#set the pause time between every click
    pyautogui.PAUSE = random.randint(20,30)
    pyautogui.FAILSAFE = True

#在函式中重複呼叫，重複按4組
#use resursive function to repeat calling the function
    for i in range(5):
        pyautogui.click(target)
        pyautogui.click(target)
        pyautogui.click(target)
        #在此檢查RGB 三色，
        now_pix = pyautogui.screenshot().getpixel((target))
        if now_pix == target_pix:
            pyautogui.click(target)
        else:
            pass
        pyautogui.click(target)



time.sleep(2400)
AutoClick()
sched = BlockingScheduler()
sched.add_job(AutoClick, 'interval', minutes=50)
sched.start()