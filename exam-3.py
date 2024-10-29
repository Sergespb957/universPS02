import requests

# URL для отправки POST-запроса
url = "https://jsonplaceholder.typicode.com/posts"

# Данные, которые будут отправлены в POST-запросе
data = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}

# Отправляем POST-запрос с данными
response = requests.post(url, json=data)

# Печатаем статус-код ответа и содержимое ответа
print("Status Code:", response.status_code)
print("Response JSON:", response.json())
