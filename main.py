from os import close
from scraping import scraping
from mail import gmail_send

"""Acquisition information adjustment"""
res = scraping()

""" Mail body settings（editing required）"""
To = "hogehoge@gmail.com(Please enter the email address to which you want to send the file.)"
Subject = "subject of the email"
MailBody = res

"""Seting savedate (No editing required)"""


def checktext():
    f = open("savedata.txt", "r")
    checkdata = f.read()
    f.close()
    return checkdata


text = checktext()


def writedata(data):
    f = open("savedata.txt", "w")
    f.write(data)
    f.close()


if text == res:
    print("No update.")
else:
    print("Get to update！")
    writedata(res)
    gmail_send(To, Subject, MailBody)
