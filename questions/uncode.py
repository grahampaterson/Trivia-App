import unidecode


def remove_non_ascii(text):
    return unidecode(unicode(text, encoding = "utf-8"))

read = open("triviaplaying.txt", "r")
write = open("triviaplaying-decoded.txt", "w")

for line in read:
    write.write(remove_non_ascii(line))

read.close()
write.close()
