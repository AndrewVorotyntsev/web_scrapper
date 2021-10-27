FROM python:3.7

# Создаем директорию
RUN mkdir -p /app/
# Переход в каталог
WORKDIR /app/

# Копировать с нашей машины (.) в контейнер
COPY . /app/
# Устанавливаем зависмости
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

# Указываем переменную окружения -- часовой пояс
#ENV TZ Europe/Moscow
# Второй вариант при запуске указать -e TZ=Europe/Moscow

# Делает при запуске контейнера
CMD ["python","main.py"]