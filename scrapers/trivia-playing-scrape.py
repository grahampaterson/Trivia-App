# from lxml import html
import os
import sys
from bs4 import BeautifulSoup
import requests
import time
import random

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


# tags a single URL as an argument and scrapes that url for all p tags contents
# all p tags are then parsed for questions and answers and add as a dict to a
# list and then returned
def parse_questions(url):

    all_questions = []

    base = "http://www.triviaplaying.com/"

    # DEBUGGING print current url for error handling
    # print(base + url)

    # get page data from supplied url
    quiz = requests.get(base + url)

    # convert to parsable soup object
    quiz_soup = BeautifulSoup(quiz.content, 'html.parser')

    # get all p tags with body tag
    trivia = quiz_soup.body.find_all("p")

    # loop through paragraph tags finding questions and answers
    for line in trivia:
        # if len(line.contents) == 2:
        #
        #     # get answers from br tag otherwise skip
        #     try:
        #         a = line.br.get_text()
        #     except AttributeError:
        #         print("Error found no br tag in ", end="")
        #         print(line)
        #         continue
        #
        #     # Strip unecessary line breaks etc
        #     a = a.replace("\n", "")
        #     a = a.replace("\r", "")
        #     a = a.replace("\r\n", "")
        #
        #     q = line.contents[0]
        #
        #     # strip newline
        #     q = q.replace("\n", "")
        #     q = q.replace("\r", "")
        #     q = q.replace("\r\n", "")
        #
        #     all_questions.append({"q": q, "a": a})
        p_text = line.get_text()
        if p_text.find("A:") == -1:
            continue
        else:
            p_text = p_text.replace("\n", "")
            p_text = p_text.replace("\r", "")
            p_text = p_text.replace("\r\n", "")
            answer = p_text.find("A:")
            q = p_text[:answer]
            a = p_text[answer:]

            print(q)
            print(a)

        all_questions.append({"q": q, "a": a})

    return all_questions


# takes a list of dicts with keys "q", "a" and "url" and writes them to file
# on separate lines
def write_file(q_list, url):

    # writes every quiz to one file
    filename = "triviaplaying.txt"
    f = open(filename, "a")

    f.write(url + "\n")
    for line in q_list:
        f.write("Q: " + line["q"] + "\n" + line["a"] + "\n")
    f.write("\n")
    f.close

# "main" function
# start_time = time.time()
url_list = scrape_urls()
# num_of_pages = len(url_list)
# counter = 0
for url in url_list:
#     print(str(num_of_pages - counter) + " pages left to scrape")
    write_file(parse_questions(url), url)
#     counter += 1
#     # if counter == 6:
#     #     break
#     pause = random.randrange(5, 30)
#     print("Pausing for " + str(pause) + " seconds")
#     time.sleep(pause)
#     print("Total time elapsed " + str(time.time() - start_time))
