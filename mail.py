""" import(No editing required) """
import os
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header
from email.mime.text import MIMEText
import smtplib
from scraping import scraping
charset = "iso-2022-jp"

"""Acquisition information adjustment"""
res = scraping()

""" Mail body settings（editing required）"""
To = "hogehoge@gmail.com(Please enter the email address to which you want to send the file.)"
Subject = "subject of the email"
MailBody = res


def gmail_send(To, Subject, MailBody):
    """ Mail settings（editing required）"""
    # connecting SMTP server・login information
    my_mail = "fugafuga@gmail.com"
    app_password = "pgvyuvbqxzeykrph"
    # Enter the address of the gmail account you created and the app password.
    smtp = smtplib.SMTP("smtp.gmail.com", 587)

    """ Mail body（No editing required）"""
    From = my_mail
    Atesaki = To
    Kenmei = Subject
    Body = MailBody

    msg = MIMEMultipart()
    msg.attach(MIMEText(Body))
    msg["Subject"] = Header(Kenmei.encode(charset), charset)

    """ connecting smtp server（No editing required）"""
    smtp.ehlo()
    smtp.starttls()
    smtp.login(my_mail, app_password)
    smtp.sendmail(From, Atesaki, msg.as_string())
    smtp.quit()

    print("sent to mail")
