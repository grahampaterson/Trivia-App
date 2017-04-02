import os
import sys

f = open('weakest-link.txt', 'r')

for line in f:
    if line[0] == "\n":
        continue
    end_question = line.find("?")
    start_ans = line.find("(") + 1
    end_ans = line.find(")")
    q = line[0:end_question + 1]
    a = line[start_ans:end_ans]
    print(q + ": " + a)


f.close()
