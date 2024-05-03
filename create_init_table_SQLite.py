import sqlite3, pathlib, sys
from sqlite3 import Error, Connection

from contextlib import contextmanager

@contextmanager
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = sqlite3.connect(db_file)
    yield conn
    conn.rollback()
    conn.close()

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

    module_file_name = sys.argv[0]
    module_path = pathlib.Path(module_file_name).parent
    database = module_path / 'my_database.db'
    print(f'local SQlite database file :{database}')

    # Створення таблиці users
    sql_table_users = '''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        fullname VARCHAR(100),
                        email VARCHAR(100) UNIQUE) ;'''

    # Створення таблиці status
    sql_table_status = '''CREATE TABLE IF NOT EXISTS status (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name VARCHAR(50) UNIQUE ) ;'''

    # Створення таблиці tasks
    sql_table_tasks = '''CREATE TABLE IF NOT EXISTS tasks (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title VARCHAR(100),
                        description TEXT,
                        status_id INTEGER,
                        user_id INTEGER,
                        FOREIGN KEY (status_id) REFERENCES status(id),
                        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE) ;'''


    with create_connection(database) as conn:
        if conn is not None:
			# create projects table
            create_table(conn, sql_table_users)
			# create tasks table
            create_table(conn, sql_table_status)

            create_table(conn, sql_table_tasks)

            print("Success to create DB file")
        else:
            print("Error! cannot create the database connection.")
