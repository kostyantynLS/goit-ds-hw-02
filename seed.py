import sqlite3, pathlib, sys
import faker, random

from sqlite3 import Error, Connection

from contextlib import contextmanager

@contextmanager
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = sqlite3.connect(db_file)
    yield conn
    conn.rollback()         # rollback all uncommited changes
    conn.close()

#filling users table
MAX_USERS = 40
MAX_STATUS = 3
MAX_TASKS = 30

fake_usernames = []
fake_emails = list()
fake_status = list()
fake_tasks = list()

def Generate_users(amount = MAX_USERS):
# users table
    for _ in range(amount):
        while True:
            name = fakes.name()
            if not name in fake_usernames:
                break
        fake_usernames.append(name)
        
        while True:
            email = '_'.join(name.split(" "))+'_'+fakes.email()
            if not email in fake_emails:
                break
        fake_emails.append(email)

def Append_users(conn, full_names, emails, amount = MAX_USERS):
    cur = conn.cursor()
    print(f'appending {amount} users ...')
    for idx in range(amount):
        try:
            # вставляємо дані про співробітників
            cur.execute("INSERT INTO users (fullname, email) VALUES (?, ?)", (full_names[idx], emails[idx]))
        except:
            print(f'insert error. duplicate value found ({idx})')
    #conn.commit()

def Generate_status(amount = MAX_STATUS):
    statuses = [('new'), ('in progress'), ('completed')]
    for idx in range(amount):
        fake_status.append(statuses[idx])

def Append_status(conn, statuses, amount = MAX_STATUS):
    # UNIQUE values, only at once!
    cur = conn.cursor()
    print(f'appending {amount} statuses ...')
    for idx in range(amount):
        try:
            value = statuses[idx]
            cur.execute("INSERT OR IGNORE INTO status (name) VALUES (?)", (value, ) )
        except:
            print('some error happen =)')
    #conn.commit()

def Generate_tasks(amount = MAX_TASKS):
    for idx in range(amount):
        title = fakes.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
        description = fakes.paragraph(nb_sentences=3, variable_nb_sentences=True, ext_word_list=None)
        status_id = random.randint(1, MAX_STATUS)
        user_id = random.randint(1, MAX_USERS)
        fake_tasks.append((title, description, status_id, user_id))

def Append_tasks(conn, fake_tasks, amount = MAX_TASKS):
    cur = conn.cursor()
    print(f'appending {amount} tasks ...')
    for idx in range(amount):
        try:
            # вставляємо задачі
            cur.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (?, ?, ?, ?)", 
                (fake_tasks[idx][0], 
                 fake_tasks[idx][1],
                 fake_tasks[idx][2],
                 fake_tasks[idx][3],))
        except:
            print(f'insert error. duplicate value found ({idx})')


# main module
if __name__ == '__main__':

    module_file_name = sys.argv[0]
    module_path = pathlib.Path(module_file_name).parent
    database = module_path / 'my_database.db'
    print(f'local SQlite database file :{database}')

    #init Faker module
    fakes = faker.Faker()

    with create_connection(database) as conn:
        if conn is not None:
			
            #update users
            Generate_users(MAX_USERS)
            Append_users(conn, fake_usernames, fake_emails, MAX_USERS)
            # statuses
            Generate_status(MAX_STATUS)
            Append_status(conn, fake_status, MAX_STATUS)
            #tasks
            Generate_tasks(MAX_TASKS)
            Append_tasks(conn, fake_tasks, MAX_TASKS)
            #finish
            conn.commit()
        else:
            print("Error! cannot create the database connection.")
