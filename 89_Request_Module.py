import requests
import os

# url = "https://jsonplaceholder.typicode.com/posts"
# data = {
#     "userId": 1,
#     "id": 1,
#     "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
#     "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
# }
# response = requests.post(url, json=data)
# print(response.text)


response = requests.get("https://www.google.com/")
# for Parsing a web page we use Beautiful Soup(bs4) module
from bs4 import BeautifulSoup

soup = BeautifulSoup(response.text, 'html.parser')

data = None
for script in soup.findAll("script"):
    data = soup.script.prettify()
    print(data)
# above code is used to scrap the code which is in mixed form
