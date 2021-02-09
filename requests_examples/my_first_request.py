import requests
import json
# получаем все посты
res = requests.get("https://jsonplaceholder.typicode.com/posts")
print(res.status_code)
print(res.json())

# получаем 1 пост
res = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(res.status_code)
print(res.json())

# создаем пост
payload = {
    'title': 'Запрос из requests',
    'body': 'Этот запрос сделан при помощи библиотеки requests',
    'userId': '101'
}
headers_params = {
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla',
}
res = requests.post("https://jsonplaceholder.typicode.com/posts", headers=headers_params, data=json.dumps(payload))
print(res.status_code)
print(res.json())

# удаляем пост
# получаем 1 пост
res = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
print(res.status_code)
print(res.json())
