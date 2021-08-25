""" インポート文(編集不要) """
import os
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header
from email.mime.text import MIMEText
import smtplib
from scraping import scraping
charset = "iso-2022-jp"

"""スクレイピング取得情報調整"""
res = scraping()

""" メール本文定義（要編集）"""
To = "hogehoge@gmail.com(送信したい相手のメールアドレスを入れてください)"
Subject = "メールの件名"
MailBody = res
# FileName = 'ファイル名.docx'

# もしファイルをメールで送信したければ⬇にある”””添付ファイル”””のコメントアウトを解除して要微調整


def gmail_send(To, Subject, MailBody):
    """ メール設定（要編集）"""
    # SMTPサーバー接続・ログイン情報
    my_mail = "fugafuga@gmail.com"
    app_password = "pgvyuvbqxzeykrph"
    # read.meの内容を参考に作成した送信用gmailアカウントのアドレスと二段階認証パスワードを入力
    smtp = smtplib.SMTP("smtp.gmail.com", 587)

    """ メール本文（編集不要）"""
    From = my_mail
    Atesaki = To
    Kenmei = Subject
    Body = MailBody

    # メール本文を読込
    #msg = MIMEText(Body,"plain",charset)
    msg = MIMEMultipart()
    msg.attach(MIMEText(Body))
    msg["Subject"] = Header(Kenmei.encode(charset), charset)

    """ 添付ファイル（編集不要）"""
    # ファイルディレクトリ指定()
#     filename = FileName
#     filepath = os.path.basename(filename)

#     # ファイル読込
#     with open(filename, "rb") as f:
#         AtchFile = MIMEApplication(f.read())

#     # ファイル添付
#     AtchFile.add_header("Content-Disposition", "attachment", filename=filepath)
#     msg.attach(AtchFile)

    """ メールサーバー接続（編集不要）"""
    # サーバー・ポート接続
    smtp.ehlo()
    # TLS暗号化
    smtp.starttls()
    # SMTPサーバーログイン
    smtp.login(my_mail, app_password)
    # メール送信
    smtp.sendmail(From, Atesaki, msg.as_string())
    # SMTPサーバー遮断
    smtp.quit()

    print("メールを送信しました。")
