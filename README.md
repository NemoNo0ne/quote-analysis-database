# Парсер Цитат

Этот проект предназначен для сбора и хранения цитат из веб-страницы в базу данных PostgreSQL.

## Описание

Скрипт парсит цитаты с сайта [quotes.toscrape.com](http://quotes.toscrape.com/) и сохраняет их в базе данных PostgreSQL. Проект включает в себя создание таблицы для хранения цитат и авторов, а также выполнение простых SQL-запросов для анализа данных.
## Использование

1. Убедитесь, что у вас установлен PostgreSQL и создана база данных.
2. Настройте параметры подключения к базе данных в коде:
   ```
   conn = psycopg2.connect(
    dbname='ваша_база',
    user='ваш_пользователь',
    password='ваш_пароль',
    host='localhost',
    port='5432')
4. Запустите скрипт, чтобы собрать цитаты и сохранить их в базе данных.

## Анализ данных
После завершения парсинга скрипт выполняет анализ данных, который включает:
- Подсчет общего количества цитат.
- Вывод топ-5 авторов с наибольшим количеством цитат.

