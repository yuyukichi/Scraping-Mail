# Scraping-Mail
Over view:This is a scraping program that will scrape and send any updates to a specified email address in the form of gmail.
<img width="1079" alt="scraiping" src="https://user-images.githubusercontent.com/66237437/130757792-4d9afa28-6ff0-4651-b02c-fd29b61ad7d0.png">

<h1>Use Step</h1>
<h3>①Instal scraiping-Mail</h3>

```
git clone git@github.com:yuyukichi/Scraping-Mail.git
```
<h3>②create new GmailAcount</h3>
https://support.google.com/mail/answer/56256?hl=ja
<h3>③setting two-step verification to GmailAcount</h3>
https://support.google.com/accounts/answer/185839?hl=ja&co=GENIE.Platform%3DDesktop<br>
※Please make a note to password.
<img width="649" alt="二段階認証" src="https://user-images.githubusercontent.com/66237437/130762052-7983a8b5-6a92-43c1-84a1-b06d42f6cd45.png">
<h3>④Edit main.py and mail.py in the downloaded Scraping-Mail.</h3>

``` mail.py
""" Mail body settings（editing required）"""
To = "hogehoge@gmail.com(Please enter the email address to which you want to send the file.)"
Subject = "subject of the email"
MailBody = res
```
Edit Variable To and Variable Subject.<br>
※Edit both main.py and mail.py.

``` mail.py
def gmail_send(To, Subject, MailBody):
    """ Mail settings（editing required）"""
    # connecting SMTP server・login information
    my_mail = "fugafuga@gmail.com"
    app_password = "pgvyuvbqxzeykrph"
    # Enter the address of the gmail account you created and the app password.
```
Edit my_mail and app_password to the gmail account you created.

<h3>⑤Edit scraping.py in the downloaded Scraping-Mail.</h3>

``` scraping.py
def scraping():
    url = 'https://www.hogehoge.co.jp/company/news/'
    # The url you want to get.

    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    elems = soup.find_all('a', class_='class__link')
    # Specify html elements and classes
    return str(elems[0].contents[0])+str(elems[0].attrs["href"])
```
1.Set the ``url`` to the URL of the site you want to scrape.<br>
2.Set the html tag and class to be retrieved as the argument of ``soup.find_all``

<h3>⑤Let run main.py!
    
``` 
python main.py
```
   
Environment：python3
(It has been tested in a mac environment.)
<p>License:MITLICENSE</p>
