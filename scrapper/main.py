import requests
from bs4 import BeautifulSoup

import psycopg2


def try_connect():
    # Подключиться к существующей базе данных
    connection = psycopg2.connect(user="postgres",
                                  # пароль, который указали при установке PostgreSQL
                                  password="1111",
                                  # в качестве ip адреса можно ипользовать название контейнера
                                  host="db",
                                  port="5432",
                                  database="postgres")
    return connection


def delete_table(cursor):
    create_table_query = 'DROP TABLE IF EXISTS vacancy'
    # Выполнение команды: это создает новую таблицу
    cursor.execute(create_table_query)


def create_table(cursor):
    # SQL-запрос для создания новой таблицы
    create_table_query = '''CREATE TABLE IF NOT EXISTS vacancy (
            id serial NOT NULL PRIMARY KEY,
            title VARCHAR (100) NOT NULL,
            company VARCHAR (100) NOT NULL,
            location VARCHAR (100) NOT NULL
        );'''
    # Выполнение команды: это создает новую таблицу
    cursor.execute(create_table_query)


def insert_item(cursor, title, company, location):
    # Выполнение SQL-запроса для вставки даты и времени в таблицу
    insert_query = """ INSERT INTO vacancy (title, company, location)
                              VALUES (%s, %s, %s)"""
    founded_vacancy = (title, company, location)
    cursor.execute(insert_query, founded_vacancy)
    connection.commit()
    print("1 элемент успешно добавлен")


# Подключаемся к базе данных
connection = try_connect()

# Получаем курсор
cursor = connection.cursor()

# Удаляем таблицу, чтобы потом записать в нее актаульные данные
delete_table(cursor)

# Создаем таблицу
create_table(cursor)

# Сайт, с которого нужно получить данные
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

# Элементы, которые содержат информацию
job_elements = soup.find_all('div', class_="card-content")

for job_element in job_elements:
    title = job_element.find("h2", class_='title').text.strip()
    company = job_element.find("h3", class_='company').text.strip()
    location = job_element.find("p", class_='location').text.strip()

    insert_item(cursor, title, company, location)

