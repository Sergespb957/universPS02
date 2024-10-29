import requests

# Задаем URL API и параметры запроса
url = "https://jsonplaceholder.typicode.com/posts"
params = {
    "userId": 1  # Фильтрация данных по userId = 1
}

# Отправляем GET-запрос с параметрами
response = requests.get(url, params=params)

# Проверяем успешность запроса и выводим записи
if response.status_code == 200:
    data = response.json()  # Преобразуем ответ в JSON формат
    print("Полученные записи для userId=1:")
    for post in data:
        print(post)
else:
    print(f"Ошибка: статус-код {response.status_code}")
