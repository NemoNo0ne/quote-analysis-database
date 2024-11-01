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

## Примечание
Использовал rollback(), так как во время выполнения программы может возникнуть ошибка (например, синтаксическая ошибка в SQL-запросе), и чтобы отменить изменения, сделанные до этой ошибки, вызывается conn.rollback().
cursor — это объект в памяти компьютера с методами для проведения SQL команд, хранения итогов их выполнения и методов доступа к ним.

## Заметки

Этот проект был разработан для учебных целей и демонстрирует навыки работы с парсингом данных, использованием библиотек Python (requests и BeautifulSoup) и взаимодействием с базой данных PostgreSQL. В процессе работы был реализован сбор цитат с веб-сайта, их сохранение в базе данных, а также простой анализ данных для подсчета общего количества цитат и определения топ-5 авторов с наибольшим числом цитат.
