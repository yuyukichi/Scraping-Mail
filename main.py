from os import close
from scraping import scraping
from mail import gmail_send

"""スクレイピング取得情報調整"""
res = scraping()

""" メール本文情報（mail.pyの同内容をコピー＆ペーストしてください）"""
To = "hogehoge@gmail.com(送信したい相手のメールアドレスを入れてください)"
Subject = "メールの件名"
MailBody = res
# FileName = 'ファイル名.docx'

"""編集不要"""


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
    print("更新なし！")
else:
    print("更新があります！")
    writedata(res)
    gmail_send(To, Subject, MailBody)

# res[0]でコンテンツ,res[1]でurl
