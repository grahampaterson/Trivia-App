from flask import Flask, render_template, url_for, jsonify, request
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
def index():
    # get 10 random numbers from the length of the database
    db_length = Question.query.count()

    # iterate over random numbers and get corrosponding row from database
    questions = []
    for x in random.sample(range(db_length), 20):
        # TODO add error handling for if row doesn't exist
        row = Question.query.get(x)
        questions.append({"id": row.id, "q": row.question, "a": row.answer,})

    return render_template("index.html", questions=questions)

@app.route('/ajax_test')
def ajax_test():
    id = request.args.get('id', 'default')
    # TODO add functionailty to add reports to database
    print(id)
    return jsonify(something="whatever")
