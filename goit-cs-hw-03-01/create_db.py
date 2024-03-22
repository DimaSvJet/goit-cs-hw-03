import sqlite3
from connect import create_connection, database
from create_table import sql_create_users_table, sql_create_status_table, sql_create_tasks_table

def create_db():
    # створюємо з'єднання з БД (якщо файлу з БД немає, він буде створений)
    with create_connection(database) as con:
        cur = con.cursor()
        
        # виконуємо скрипт із файлу, який створить таблиці в БД
        cur.executescript(sql_create_users_table)
        cur.executescript(sql_create_status_table)
        cur.executescript(sql_create_tasks_table)

if __name__ == "__main__":
    create_db()
