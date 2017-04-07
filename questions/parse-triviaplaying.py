import sqlite3

# function to parse text file for qustion and answer combinations
# questions are indicated by line starting with Q: and answers A:
# urls contain the string .htm
# returns a list of dicts containing above keys/values
def parse_text(infile):

    parsed_info = []

    # open file
    f = open(infile, "r")

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
        # insert_sql(q, a, url)

        # adds parsed elements to dict
        parsed_info.append({'q': q, "a": a, "url": url})

    return parsed_info

    f.close()

# sqlite function that takes 4 arguments of a database name question,
# answer and url and adds them to a sqlite table, if the
# table doesn;t exist it is created

def insert_sql(db, q, a, url):

    # connect to database and insert arguments
    conn = sqlite3.connect(db)
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS questions (id INTEGER PRIMARY KEY AUTOINCREMENT, question TEXT, answer TEXT, url TEXT)''')

    c.execute('INSERT INTO questions (question, answer, url) VALUES (?, ?, ?)', (q, a, url))
    conn.commit()

    conn.close()

example_dict = {'q': "question222", "a": "answer333", "url": "url333",}
insert_sql("testdb.sqlite", example_dict['q'], example_dict['a'], example_dict['url'])

# parse_text("triviaconverted.txt")
