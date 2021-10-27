from flask import Flask, render_template
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


app = Flask(__name__)

headings = ("Title", "Company", "Location")

# Подключаемся к базе данных
connection = try_connect()

@app.route('/')
def table():
    # Получаем курсор
    cursor = connection.cursor()

    cursor.execute("SELECT title, company, location FROM vacancy")
    data = cursor.fetchall()
    return render_template('table.html', headings=headings, data=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)