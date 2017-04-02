import os
import sys

def weakest_link_parse():
    f = open('weakest-link.txt', 'r')

    all_questions = []

    for line in f:
        if line[0] == "\n":
            continue
        end_question = line.find("?")
        start_ans = line.find("(") + 1
        end_ans = line.find(")")
        q = line[0:end_question + 1]
        a = line[start_ans:end_ans]
        # print(q + ": " + a)
        all_questions.append({"q": q, "a": a})

    print(all_questions[1])
    print(all_questions[50])

    f.close()

    return all_questions

weakest_link_parse()
