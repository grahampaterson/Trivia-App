from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
import os
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///triviadb.sqlite'
db = SQLAlchemy(app)

# defining sqlalchemy ORM
class Question(db.Model):
    __tablename__ = "questions"
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String)
    answer = db.Column(db.String)

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

@app.route('/')
def hello_world():
    # get 10 random numbers from the length of the database
    db_length = Question.query.count()

    questions = []
    for x in random.sample(range(db_length), 20):
        row = Question.query.get(x)
        questions.append({"q": row.question, "a": row.answer,})

    return render_template("index.html", questions=questions)
