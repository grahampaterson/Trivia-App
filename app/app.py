from flask import Flask, render_template, url_for, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os
import random

# test

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///triviadb.sqlite'
db = SQLAlchemy(app)

# defining sqlalchemy ORM
class Question(db.Model):
    __tablename__ = "questions"
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String)
    answer = db.Column(db.String)
    status_id = db.Column(db.Integer)

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
        self.status_id = status_id


@app.route('/')
def index():
    # iterate over random numbers and get corrosponding row from database
    questions = []

    # query database for random sample of questions with status id 0
    all_qs = random.sample(Question.query.filter_by(status_id='0').all(), 20)

    # iterate over random sample to pass to template
    for row in all_qs:
        questions.append({"id": row.id, "q": row.question, "a": row.answer,})

    return render_template("index.html", questions=questions)

@app.route('/report')
def report():
    # if the server receives an ID as a get request the question is reported
    # and changed to status "1" for reported
    id = request.args.get('id', 'default')
    if id == "default":
        return jsonify(nothing="nothing")
    else:
        # change old question status
        Question.query.filter_by(id=id).first().status_id = 1
        db.session.commit()
        # get a new question from the database
        # TODO getting random question needs to be optimised
        new_q = random.choice(Question.query.filter_by(status_id='0').all())
        replacement = {'id': new_q.id, 'q': new_q.question, 'a': new_q.answer}
        print(id)

    return jsonify(newq=replacement)
