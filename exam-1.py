import requests

# Задаем URL API с параметром поиска
url = "https://api.github.com/search/repositories"
params = {
    "q": "html in:readme",  # Параметр поиска, ищет репозитории с упоминанием 'html' в описании
}

# Отправляем GET-запрос
response = requests.get(url, params=params)

# Печатаем статус-код ответа
print("Status Code:", response.status_code)

# Печатаем содержимое ответа в формате JSON
try:
    data = response.json()  # Преобразуем ответ в JSON
    print("Response JSON:", data)
except ValueError:
    print("Ошибка при преобразовании ответа в JSON.")
