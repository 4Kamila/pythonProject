import urllib.request
import requests
from bs4 import BeautifulSoupimport requestsresponse = requests.get("https://coinmarketcap.com/")if response.status_code == 200:    soup = BeautifulSoup(response.text, features="html.parser")    soup_list = soup.find_all("a", {"href": "/currencies/bitcoin/markets/"})    res = soup_list[0].find("span")    print(res.text)
res_parse_list = []
# opener = urllib.request.build_opener()
# response = opener.open("https://httpbin.org/")
# print(response.read())

# response = requests.get("https://httpbin.org/get")
# print(response.text)
#
# print(f"Datatype - {type(response.text)}")

# response = requests.post("https://httpbin.org/"
#                          "post", data="Test data",
#                           headers={"h1": "Test title"})
# response = requests.get("https://coinmarketcap.com/")
# response_text = response.text
# response_parse = response_text.split("<span>")
# for parse_elem_1 in response_parse:
#     if parse_elem_1.startswith("$"):
#         for parse_elem_2 in parse_elem_1.split("</span>"):
#             if parse_elem_2.startswith("$") and parse_elem_2[1].isdigit():
#                 res_parse_list.append((parse_elem_2))
# bitcoin_exchange_rate = res_parse_list[0]
# print(bitcoin_exchange_rate)

# print(response.text)
