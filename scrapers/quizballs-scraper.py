import requests
from bs4 import BeautifulSoup
from sqlitecreator import insert_sql

# scrape quizballs function takes no arguments and simply scrapes all 461 original
# quizzes for questions and answers and outputs everything to a write document
def scrape_quizballs(page_num):

    all_questions = []

    # getting the urls
    baseurl = "http://www.businessballs.com/quizballs/quizballs"
    url = "http://www.businessballs.com/quizballs/quizballs" + str(page_num) + "_free_trivia_quiz_questions_answers.htm"

    # getting pge through requests and doing beautiful soup stuff
    page = requests.get(url)
    html = page.content
    soup = BeautifulSoup(html, "html.parser")

    # finding all the li tags (where the questions are) and formatting them
    li_tags = soup.article.find_all("li")
    for tag in li_tags:

        # removing weird spacing and line breaks
        space = " "
        tag_text = tag.get_text().strip()

        tag_text = tag_text.replace("\n", "")
        tag_text = tag_text.replace("\r", "")
        tag_text = tag_text.replace("\r\n", "")

        qa_string = space.join(tag_text.split())

        # split question and asnwer based on "?" character
        divider = qa_string.find("?")
        q = qa_string[:divider + 1]
        a = qa_string[divider + 2:]
        all_questions.append({"q": q, "a": a, "info": url})

    return all_questions

# print(scrap_quizballs())

# writes scraped data to file
def write_file(quiz_list, output_name):
    f = open(output_name, "a")

    for line in quiz_list:
        f.write("Q: " + line["q"] + "\n")
        f.write("A: " + line["a"] + "\n")
        f.write("URL: " + line["info"] + "\n")

    f.close()

# parses text file and otputs list of dicts
def read_txt(input_file):

    all_questions = []
    q = ""
    a = ""
    url = ""

    f = open(input_file, "r")

    for line in f:
        line = line.replace("\n", "")
        line = line.replace("\r", "")
        line = line.replace("\r\n", "")
        if line[:2] == "Q:":
            q = line[3:]
            # print(q)
        elif line[:2] == "A:":
            a = line[3:]
            # print(a)
        elif line[:4] == "URL:":
            url = line[5:]
            # print(url)
            all_questions.append({"q": q, "a": a, "info": url,})

    return all_questions

insert_sql("testdb.sqlite", read_txt("quizballs.txt"))
