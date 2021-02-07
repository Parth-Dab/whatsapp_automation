import pywhatkit
import getpass
import datetime

print("whats app automate")
msg = input('input the message')
hour = int(input("enter the hour:"))
minutes = int(input("enter the minutes:"))
phone = getpass.getpass(prompt="enter phone number:", stream=None)
pywhatkit.sendwhatmsg(phone,msg,hour,minutes)











