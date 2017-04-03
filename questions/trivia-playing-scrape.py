# from lxml import html
import os
import sys
from bs4 import BeautifulSoup
import requests

# get all the links to the different trivia pages
# and return list of urls
def scrape_urls():
    urls = []
    page = requests.get('http://www.triviaplaying.com/include/rightside.html')
    html = page.content

    soup = BeautifulSoup(html, "html.parser")

    link = soup.find_all("a")

    # iterate over urls from home page and append to list
    for a in link:
        urls.append(a.attrs['href'])

    return urls


# parse document for paragraph tags containing questions
def parse_questions(url):

    all_questions = []

    base = "http://www.triviaplaying.com/"

    # get url for quiz and scrape p tags
    quiz = requests.get(base + url)
    # quiz_content = quiz.content
    quiz_soup = BeautifulSoup(quiz.content, 'html.parser')
    trivia = quiz_soup.find_all("p")

    # loop through paragraph tags finding questions and answers
    for line in trivia:
        if len(line.contents) > 1:
            q = line.contents[0].string
            # strip newline
            q = q.replace("\n", "")
            q = q.replace("\r", "")
            q = q.replace("\r\n", "")

            a = line.contents[1].string[4:]

            all_questions.append({"q": q, "a": a})

    return all_questions

sample = [{"q": "question", "a": "answer"}]

# takes a list of dicts with keys "q" and "a" and writes them to file quiz.txt
def write_file():
    f = open("quiz.txt", "w")
    for line in sample:
        f.write(line["q"] + line["a"])
    f.close

# parse_questions(link[0].attrs['href'])
