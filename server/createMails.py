import requests
import json
from bs4 import BeautifulSoup
import re
import sqlite3
from requests.models import get_auth_from_url
import os.path

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,/;q=0.8',
'Accept-Language': 'de,en-US;q=0.7,en;q=0.3',
'Connection': 'keep-alive',
'Upgrade-Insecure-Requests': '1',
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'cross-site',
'Cache-Control': 'max-age=0',
}


response = requests.get('https://anonbox.net/de/', headers=headers)
response = response.content.decode('utf-8')


class getMail:
    def __init__(self) -> None:
        try:
            self.db = sqlite3.connect('data.db')
            self.conn = self.db.cursor()
            print("Succesfull")

        except Exception as e:
            print(e)

    def createMail(self):
        #regex zeug und filterung
        get_link = re.findall(r"https://anonbox.net/[a-z0-9]*/[a-z0-9]*", response)
        print(get_link[0])

        remove = r"<span style='display: none' class=foobar>[a-zA-Z0-9\-]*</span>"
        remove2 = "<span></span>"
        result = re.sub(remove, '', response)
        result = re.sub(remove2, '', result)
        get_mail = re.findall(r"[a-z0-9]*@wgbn6.anonbox.net", result)
        print(get_mail[0])


        Email = 'test'
        Mailbox = 'test2'

        sql = "SELECT count(*) FROM anonymprofile WHERE Email = '{}', '{}"
        rows = self.conn.fetchone()#[0]
        print(rows)
        #if rows >0:
         #   return True
      #  else:
         #   return False
      

        sqlMail = f"INSERT INTO anonymprofile VALUES ('{Email}')"
        sqlMailbox = f"INSERT INTO anonymprofile VALUE ('{Mailbox}')"
        self.conn.execute(sqlMail, sqlMailbox)
        self.db.commit()
    
newMail = getMail()

print(newMail.createMail())






#a href="https://anonbox.net/wgbn6/i3mkoh6iuk">https://anonbox.net/wgbn6/i3mkoh6iuk</a></p></dd>
#dd><p>mu3xs347aq<span style='display: none' class=foobar>-test2-</span>@wgbn6<span></span>.<span style='display: none' class=foobar>nixda</span>anonbox.<span style='d


