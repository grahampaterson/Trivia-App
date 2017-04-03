# from lxml import html
import os
import sys
from bs4 import BeautifulSoup
import requests

base = "http://www.triviaplaying.com/"

# get all the links to the different trivia pages
page = requests.get('http://www.triviaplaying.com/include/rightside.html')
html = page.content

soup = BeautifulSoup(html, "html.parser")

link = soup.find_all("a")

# iterate over urls from home page
# for a in link:
#     print(a.attrs['href'])

f = open("quiz.txt", "w")

# parse document for paragraph tags containing questions
# print(base + link[0].attrs['href'])
quiz = requests.get(base + link[0].attrs['href'])
quiz_content = quiz.content
# print(quiz_content)
quiz_soup = BeautifulSoup(quiz_content, 'html.parser')
# print(quiz_soup)
trivia = quiz_soup.find_all("p")

for q in trivia:
    print(q.contents)

f.close()
