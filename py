import requests
from bs4 import BeautifulSoup

def parse_website(url):
    # Отправляем GET-запрос на сайт
    response = requests.get(url)

    # Проверяем успешность запроса
    if response.status_code == 200:
        # Получаем HTML-код страницы
        html = response.text
        print(html)

        # Инициализируем объект BeautifulSoup для парсинга
        soup = BeautifulSoup(html, 'html.parser')

        # Находим все заголовки статей (пример)
        article_headings = soup.find_all('h2', class_='title')


        # Выводим заголовки статей
        for heading in article_headings:
            print(heading.text)

    else:
        print(f"Ошибка {response.status_code}: Не удалось получить доступ к странице.")

# Пример использования
url_to_parse = 'import requests
from bs4 import BeautifulSoup

def parse_website(url):
    # Отправляем GET-запрос на сайт
    response = requests.get(url)

    # Проверяем успешность запроса
    if response.status_code == 200:
        # Получаем HTML-код страницы
        html = response.text
        print(html)

        # Инициализируем объект BeautifulSoup для парсинга
        soup = BeautifulSoup(html, 'html.parser')

        # Находим все заголовки статей (пример)
        article_headings = soup.find_all('h2', class_='title')


        # Выводим заголовки статей
        for heading in article_headings:
            print(heading.text)

    else:
        print(f"Ошибка {response.status_code}: Не удалось получить доступ к странице.")

# Пример использования
url_to_parse = 'http://dielf20142.temp.swtest.ru/'
parse_website(url_to_parse)'
parse_website(url_to_parse)
