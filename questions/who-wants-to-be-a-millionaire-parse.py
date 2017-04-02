import os
import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///millionaire.sqlite')

Base = declarative_base()

class Question(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(String)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


f = open('who-wants-to-be-a-millionaire-input.txt', 'r')

questions = []
new_question = ""

for line in f:
    current_line = line.strip()
    if current_line.find("#") > -1:
        # check if question over multiple lines
        if current_line.find("?") > -1:
            new_question = current_line[6:]
        else:
            current_line = current_line + " " + f.readline().strip()
            new_question = current_line[6:]
    if current_line.find("*") > -1:
        print(current_line)
    if current_line.find("Ans") > -1:
        # print(current_line[8:])
        questions.append(Question(question = new_question, answer = current_line[8:]))

session.add_all(questions)
session.commit()

# # loop through every character of file
# for x in range(25000):
#     char = f.read(1)
#
#     # if a # is found
#     if char == "#":
#         # save characters to variable
#         write = True
#
#     if write == True:
#         # check for newline char
#         if char != "\n":
#             question = question + char
#
#     if char == "?":
#         write = False
#         print(question)
#         question = ""

f.close()
