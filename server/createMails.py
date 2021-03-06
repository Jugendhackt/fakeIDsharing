

import requests
import json
from bs4 import BeautifulSoup
import re
import sqlite3
from requests.api import get
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
            self.db = sqlite3.connect('server/data.db')
            self.conn = self.db.cursor()
            print("Succesfull")

        except Exception as e:
            print(e)

    def createMail(self):
        # regex zeug und filterung
        get_link = re.findall(
            r"https://anonbox.net/[a-z0-9]*/[a-z0-9]*", response)

        remove = r"<span style='display: none' class=foobar>[a-zA-Z0-9\-]*</span>"
        remove2 = "<span></span>"
        result = re.sub(remove, '', response)
        result = re.sub(remove2, '', result)
        get_mail = re.findall(r"[a-z0-9]*@[a-z0-9]*.anonbox.net", result)
        self.getmail = get_mail
        self.get_link = get_link
        return get_mail
