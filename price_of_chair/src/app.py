__author__ = 'shiv_ashish_niranjan'

import requests
from bs4 import BeautifulSoup

request = requests.get("https://paytm.com/digitalgold")
content = request.content
soup = BeautifulSoup(content, "html.parser")

element = soup.find("div", {"class": "_24BG"})

print(element.text)

# <div class="_1cMg"><!-- react-text: 744 -->Gold @ ₹4893.34/g<!-- /react-text --><img src="https://dg-static3.paytm.com/wealthmgmt/assets/Image/reload.png" class="_2ROs"></div>