from sqlite3 import Error
from connect import create_connection, database

sql_create_users_table = """
    CREATE TABLE IF NOT EXISTS users (
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     fullname VARCHAR(100) NOT NULL,
     email VARCHAR(100) UNIQUE NOT NULL
    );
    """

sql_create_status_table = """
    CREATE TABLE IF NOT EXISTS status (
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     name VARCHAR(50) UNIQUE NOT NULL
    );
    """

sql_create_tasks_table = """
    CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT,
    title VARCHAR(100),
    status_id INT,
    user_id INT,
    FOREIGN KEY (status_id) REFERENCES status(id)
        ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(id)
        ON DELETE CASCADE
    );
    """


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        conn.commit()
    except Error as e:
        print(e)


if __name__ == '__main__':
    with create_connection(database) as conn:
        if conn is not None:
            # create users table
            create_table(conn, sql_create_users_table)
            # create users status
            create_table(conn, sql_create_status_table)
            # create tasks table
            create_table(conn, sql_create_tasks_table)
        else:
            print("Error! cannot create the database connection.")
