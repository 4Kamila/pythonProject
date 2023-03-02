from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.oschadbank.ua/currency-rate")
if response.status_code == 200:
    soup = BeautifulSoup(float(response.text, features="html.parser"))
    soup_list = soup.find_all("td")
    res = soup_list[0].find("span")
    print(float(res.text))
# class Converter:
#     def __init__(self):
#         a = int(input("Введіть бажану суму: "))
#         print(a*res.text)
# bank = Converter()
