import sqlite3

# sqlite function that takes 2 arguments of a database name,
# and a list of dicts with keys "q", "a", "info" inserted into a sqlite table, if the
# table doesn't exist it is created
def insert_sql(db, qainfo_list):

    # connect to database and insert arguments
    conn = sqlite3.connect(db)
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS questions (id INTEGER PRIMARY KEY AUTOINCREMENT, question TEXT, answer TEXT, info TEXT)''')

    # iterate through list and add dicts to database
    # TODO add error check for empty lists, incorrect data types etc...
    for x in qainfo_list:
        if len(x) == 3:
            c.execute('INSERT INTO questions (question, answer, info) VALUES (?, ?, ?)', (x['q'], x['a'], x['info']))
        elif len(x) == 2:
            c.execute('INSERT INTO questions (question, answer) VALUES (?, ?)', (x['q'], x['a']))

    conn.commit()
    conn.close()
