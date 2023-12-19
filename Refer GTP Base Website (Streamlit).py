import requests

url='https://jsonplaceholder.typicode.com/users'

respond=requests.get(url)

print(respond.text)