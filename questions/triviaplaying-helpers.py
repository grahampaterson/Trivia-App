import re
from sqlitecreator import insert_sql

# function takes an input file and an output file
# the function parses the urls at the beginning of a set of questions for a
# date format using regex, if a date is found that information is prepended to
# the beginning of the following questions until another url is found
# all data is written to output file
def format_dates(inputfile, outputfile):
    infile = open(inputfile, "r")
    outfile = open(outputfile, "w")

    date = ""

    for line in infile:
        # match lines that are URLS and include a date
        if line.find(".htm") > -1 and (line.find("-19") > -1 or line.find("-20") > -1):
            # regex to get specific date
            match = re.findall('-[12][90]..[s\-\.]', line)

            # check if multiple dates in line
            if len(match) > 1:
                highest = "0"
                for i in match:
                    if int(i[1:5]) > int(highest):
                        highest = i[1:5]
                date = highest
            else:
                # save only date portion
                date = match[0][1:5]
        # if there is a url without a date reset date variable
        elif line.find(".htm") > -1:
            date = ""
        # look for "question" lines
        elif line[0:2] == "Q:":
            # check if date property exists and update it otherwise move on
            if len(date) > 2:
                line = "Q: In " + date + " " + line[3:]

        outfile.write(line)

    infile.close()
    outfile.close()


# function to parse text file for Question and answer combinations
# questions are indicated by line starting with Q: and answers A:
# urls contain the string .htm
# returns a list of dicts containing above keys/values
def parse_text(infile):

    parsed_info = []

    # open file
    f = open(infile, "r")

    url ="no url"

    # loop through each line of file
    for line in f:
        q = ""
        a = ""
        if line[0:2] == "Q:":
            q = line
            nextline = f.readline()
            if nextline[0:2] == "A:":
                a = nextline
            else:
                continue
        elif line.find(".htm") != -1:
            url = line
            continue
        else:
            # print("IGNORE " + line)
            continue

        # adds parsed elements to dict
        parsed_info.append({'q': q, "a": a, "info": url})

    return parsed_info

    f.close()

insert_sql("testdb.sqlite", parse_text("triviadated.txt"))
# parse_text("triviaconverted.txt")
