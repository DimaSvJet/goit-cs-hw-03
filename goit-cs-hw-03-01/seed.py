import faker
from random import randint
import sqlite3
from connect import create_connection, database

fake_data = faker.Faker()

# Функції для генерації даних


def generate_users(n=10):
    """Генерує випадкові дані для таблиці користувачів"""
    users = [(fake_data.name(), fake_data.email())
             for _ in range(n)]  # тут генеруємо призвиська людей та їх email
    return users


def generate_statuses():
    """Генерує випадкові дані для таблиці статусів"""
    statuses = [('new',), ('in progress',), ('completed',)]
    return statuses


def generate_tasks(n=30):
    """Генерує випадкові дані для таблиці завдань"""
    tasks = []
    for _ in range(n):
        title = fake_data.sentence(nb_words=6)
        description = fake_data.text(max_nb_chars=200)
        status_id = randint(1, 3)
        user_id = randint(1, 10)
        tasks.append((title, description, status_id, user_id))
    return tasks


def populate_database():
    with create_connection(database) as conn:
        try:
            cur = conn.cursor()

            # Вставка користувачів
            users = generate_users()
            cur.executemany(
                "INSERT INTO users (fullname, email) VALUES (?, ?)", users)

            # Вставка статусів
            statuses = generate_statuses()
            cur.executemany("INSERT INTO status (name) VALUES (?)", statuses)

            # Вставка завдань
            tasks = generate_tasks()
            cur.executemany(
                "INSERT INTO tasks (title, description, status_id, user_id) VALUES (?, ?, ?, ?)", tasks)

            conn.commit()
            cur.close()
        except sqlite3.Error as error:
            print(error)

populate_database()

