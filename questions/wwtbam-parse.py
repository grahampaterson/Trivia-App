from sqlitecreator import insert_sql

def wwtbam_parse():

    f = open('who-wants-to-be-a-millionaire-input.txt', 'r')

    all_questions = []
    q = ""
    a = ""

    for line in f:

        # current line with whitespace removed
        current_line = line.strip()

        # check if questions line (starting with #)
        if current_line.find("#") > -1:
            # check if question over multiple lines and read next line if true
            if current_line.find("?") > -1:
                q = current_line[6:] + " "
            else:
                current_line = current_line + " " + f.readline().strip()
                q = current_line[6:] + " "

        # add later, multiple choice answers
        if current_line.find("*") > -1:
            q += current_line[1:] + ", "

        # check if answer line and append current q and a to all_questions
        if current_line.find("Ans") > -1:
            a = current_line[8:]
            all_questions.append({"q": q[:-2], "a": a, "info": "wwtbam"})

    print(all_questions[1])
    print(all_questions[50])

    f.close()

    return all_questions

insert_sql("testdb.sqlite", wwtbam_parse())
