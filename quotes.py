import psycopg2
import requests
from bs4 import BeautifulSoup

try:
    # Подключение к базе данных
    conn = psycopg2.connect(
        dbname='ваша_база',
        user='ваш_пользователь',
        password='ваш_пароль',
        host='localhost',
        port='5432'
    )
    cursor = conn.cursor()
    print("Успешное подключение к базе данных!")

    # Создаем таблицу, если она не существует
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS quotes (
                id SERIAL PRIMARY KEY,
                text TEXT UNIQUE,
                author TEXT
            )
        ''')
        conn.commit()
        print("Таблица 'quotes' создана успешно.")
    except psycopg2.errors.SyntaxError as e:
        print(f"Ошибка синтаксиса SQL при создании таблицы: {e}")
        conn.rollback()  # Откат транзакции в случае ошибки

    # Парсинг и сбор данных
    base_url = 'http://quotes.toscrape.com/'
    page = 1
    max_pages = 5
    while page <= max_pages:
        # Формируем URL для текущей страницы
        url = f'{base_url}page/{page}/'
        response = requests.get(url)
        print("Статус-код ответа:", response.status_code)
        # Проверка успешности запроса
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser') # Создаем объект BeautifulSoup для парсинга HTML
            quotes = soup.find_all('div', class_='quote') # Извлекаем все блоки с цитатами

            for quote in quotes:
                text = quote.select_one(".text").get_text(strip=True)
                author = quote.select_one(".author").get_text(strip=True)

                # Проверяем, есть ли цитата уже в базе данных
                try:
                    cursor.execute('SELECT EXISTS(SELECT 1 FROM quotes WHERE text=%s)', (text,))
                    exists = cursor.fetchone()[0] # Получаем результат запроса (True/False)

                    # Добавляем цитату, если ее еще нет в базе данных
                    if not exists:
                        cursor.execute('INSERT INTO quotes (text, author) VALUES (%s, %s)', (text, author))
                        conn.commit()
                        print(f'Цитата добавлена: {text}')
                    else:
                        print(f'Цитата уже существует: {text}')
                except psycopg2.Error as e:
                    print(f"Ошибка SQL при добавлении цитаты: {e}")
                    conn.rollback()  # Откат транзакции в случае ошибки, чтобы избежать нарушений данных
        else:
            print("Ошибка при запросе страницы:", response.status_code)
        page += 1

    # Анализ данных с SQL-запросами
    try:
        # Подсчет общего количества цитат
        cursor.execute("SELECT COUNT(*) FROM quotes")
        count_quotes = cursor.fetchone()[0]
        print(f"\nОбщее количество цитат в базе данных: {count_quotes}")

        # Топ-5 авторов с наибольшим количеством цитат
        cursor.execute('''
            SELECT author, COUNT(*) AS num_quotes 
            FROM quotes 
            GROUP BY author 
            ORDER BY num_quotes DESC 
            LIMIT 5
        ''')
        top_authors = cursor.fetchall()
        print("\nТоп-5 авторов с наибольшим количеством цитат:")
        for author, num_quotes in top_authors:
            print(f"{author}: {num_quotes} цитат")
    except psycopg2.errors.SyntaxError as e:
        print(f"Ошибка синтаксиса SQL при анализе данных: {e}")
        conn.rollback()  # Откат транзакции в случае ошибки
    except psycopg2.Error as e:
        print(f"Ошибка работы с базой данных при анализе данных: {e}")
        conn.rollback()

except psycopg2.Error as e:
    print(f"Произошла ошибка работы с базой данных: {e}")

finally:
    # Закрытие соединения и курсора
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'conn' in locals() and conn:
        conn.close()












