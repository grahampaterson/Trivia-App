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

    # print current url for error handling
    print(base + url)

    # get page data from supplied url
    quiz = requests.get(base + url)

    # convert to parsable soup object
    quiz_soup = BeautifulSoup(quiz.content, 'html.parser')

    # get all p tags with body tag
    trivia = quiz_soup.body.find_all("p")

    # loop through paragraph tags finding questions and answers
    for line in trivia:
        if len(line.contents) == 2:

            # get answers from br tag otherwise skip
            try:
                a = line.br.get_text()
            except AttributeError:
                print("Error found no br tag")
                continue

            # Strip unecessary line breaks etc
            a = a.replace("\n", "")
            a = a.replace("\r", "")
            a = a.replace("\r\n", "")

            q = line.contents[0]

            # strip newline
            q = q.replace("\n", "")
            q = q.replace("\r", "")
            q = q.replace("\r\n", "")

            all_questions.append({"q": q, "a": a})
            print(q)
            print(a)

    return all_questions

sample = [{"q": "question", "a": "answer"}]


# takes a list of dicts with keys "q" and "a" and writes them to file quiz.txt
def write_file(q_list, n):
    filename = "quiz" + str(n) + ".txt"
    f = open(filename, "w")
    for line in q_list:
        f.write(line["q"] + ": " + line["a"] + "\n")
    f.close

# "main" function
# url_list = scrape_urls()
# for url in url_list:
#     counter = 0
#     write_file(parse_questions(url), counter)

parse_questions(scrape_urls()[1])
