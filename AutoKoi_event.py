from apscheduler.schedulers.blocking import BlockingScheduler
import pyautogui
import time
import random
import smtplib
from email.mime.text import MIMEText
import json

now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
target = pyautogui.position()
print(now)


def sendallert():
    account = json.load(open('account.json', 'r', encoding='utf-8'))
    gmailUser = account['account']
    gmailPasswd = account['passwd']
    message = MIMEText('過耗體警訊!', 'plain', 'utf-8')
    message['Subject'] = '過耗體'
    message['From'] = gmailUser
    message['To'] = gmailUser
    smtp = smtplib.SMTP("smtp.gmail.com:587")
    smtp.ehlo()
    smtp.starttls()
    smtp.login(gmailUser, gmailPasswd)
    smtp.sendmail(message['From'], message['To'], message.as_string())
    print('已寄出警訊')


def overprevent(target):
    now_pix = pyautogui.screenshot().getpixel(target)
    if now_pix[0] < 100:
        pyautogui.click(target.x-170,target.y+50)
        time.sleep(600)
        print("此時過耗體")
        overtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(overtime)
        sendallert()

    return 0


def AutoClick():
    # 設定每次按按鍵中間間隔
    # set the pause time between every click
    pyautogui.PAUSE = random.randint(40, 45)
    pyautogui.FAILSAFE = True
    overprevent(target)
    # 在函式中重複呼叫，重複按4組
    # use recursive function to repeat calling the function
    for i in range(5):
        pyautogui.click(target)
        pyautogui.click(target)
        pyautogui.click(target)
        # 在此檢查RGB三色，然後比對是否是橘色
        now_pix = pyautogui.screenshot().getpixel(target)
        if now_pix[0] > 220:
            pyautogui.click(target)
        else:
            pass
        pyautogui.click(target)
        print("完成第", i, "次")
    print("迴圈結束，開始進入等待")
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(now)


# 設定延時執行的秒數
time.sleep(0)

# 開始執行程式，由於後面sched的interval排程無法執行第一次，所以我們先讓他執行一次
AutoClick()
sched = BlockingScheduler()
# 將自動點擊加入排程
sched.add_job(AutoClick, 'interval', minutes=52)
sched.start()
