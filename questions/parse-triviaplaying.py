import sqlite3

# define parsing function
def parse_text():
    # open file
    f = open("triviaconverted.txt", "r")

    url ="no url"

    # loop through each line of file
    for line in f:
        q = ""
        a = ""
        if line[0:2] == "Q:":
            q = line
            nextline = f.readline()
            if nextline[0:2] == "A:":
                a = nextline
            else:
                continue
        elif line.find(".htm") != -1:
            url = line
            continue
        else:
            # print("IGNORE " + line)
            continue

        # add q, a and url to database function
        insert_sql(q, a, url)


    f.close()

# define sqlite population function (move to separate doc later)

def insert_sql(q, a, url):
    c.execute('INSERT INTO questions (question, answer, url) VALUES (?, ?, ?)', (q, a, url))
    conn.commit()

# connect to database and create table
conn = sqlite3.connect('triviaplaying.sqlite')
c = conn.cursor()
c.execute('''CREATE TABLE questions (id INTEGER PRIMARY KEY AUTOINCREMENT, question TEXT, answer TEXT, url TEXT)''')
parse_text()


# include insert statements here

conn.close()
