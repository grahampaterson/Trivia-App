import os
import sys
# from sqlalchemy import create_engine, Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
#
# engine = create_engine('sqlite:///millionaire.sqlite')
#
# Base = declarative_base()
#
# class Question(Base):
#     __tablename__ = 'questions'
#
#     id = Column(Integer, primary_key=True)
#     question = Column(String)
#     answer = Column(String)
#
# Base.metadata.create_all(engine)
#
# Session = sessionmaker(bind=engine)
# session = Session()

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
                q = current_line[6:]
            else:
                current_line = current_line + " " + f.readline().strip()
                q = current_line[6:]

        # add later, multiple choice answers
        # if current_line.find("*") > -1:
        #     print(current_line)

        # check if answer line and append current q and a to all_questions
        if current_line.find("Ans") > -1:
            a = current_line[8:]
            all_questions.append({"q": q, "a": a})

    print(all_questions[1])
    print(all_questions[50])

    f.close()

    return all_questions
            # function to
            # questions.append(Question(question = new_question, answer = current_line[8:]))

wwtbam_parse()

# session.add_all(questions)
# session.commit()
