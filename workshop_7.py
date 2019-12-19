import datetime as dt
import re

# Text Files

# 1 You are given a file called class_scores.txt , where each line of the file contains a one-word username and a test
# score separated by spaces, like below:.
#  GWashington 83JAdams 86HWells 88
# Write code that scans through the file, adds 5 points to each test score, and outputs the user-
# names and new test scores to a new file, scores2.txt .


def ex1_practice():
    with open("files/class_scores.txt", "r") as class_scores:
        print("This is a file name: ", class_scores.name)
        class_scores_contents = class_scores.readlines()
        print(class_scores_contents)
        class_scores_contents.insert(1, "KColumbus 90\n")

    with open("files/class_scores.txt", "w") as class_scores:
        print(class_scores_contents)
        class_scores_contents_previous = "".join(class_scores_contents)
        print(class_scores_contents_previous)
        # class_scores.write(class_scores_contents_previous)

    with open("files/class_scores.txt", "r") as class_scores:
        for line in class_scores:
            print(line)


def ex1():
    new_data = []
    with open("files/class_scores.txt", "r") as class_scores:
        data = class_scores.readlines()
        for line in data:
            elements = line.split()
            print(elements)
            elements[1] = str(int(elements[1]) + 5)
            print(elements)
            with open("files/class_scores2.txt", "a") as c:
                c.write(elements[0])
                c.write(" ")
                c.write(elements[1])
                c.write("\n")


# 3. You are given a file called grades.txt , where each line of the file contains a one-word student username and three
# test scores separated by spaces, like below:.
# GWashington 83 77 54
# JAdams 86 69 90
# Write code that scans through the file and determines how many students passed all three tests.

def ex2():
    with open("files/grades.txt", "r") as grades:
        data = grades.readlines()
        for line in data:
            elem = line.split()
            print(elem)
            if int(elem[1]) > 60 and int(elem[2]) > 60 and int(elem[3]) > 60:
                print(elem[0] + " passed")
            else:
                print(elem[0] + " didn\'t pass")


# 3. You are given a file called logfile.txt that lists log-on and log-off times for users of a system. A typical
# line
# of the file looks like this:
# Van Rossum, 14:22, 14:37
# Each line has three entries separated by commas: a username, a log-on time, and a log-off time. Times are given in
# 24-hour format. You may assume that all log-ons and log-offs occur within a single workday.
# Write a program that scans through the file and prints out all users who were online for at least an hour.

def ex3():
    with open("files/logfile.txt", "r") as logfile:
        logs = logfile.read()
    logs = logs.split("\n")
    logs = [log.split(", ") for log in logs]
    print("USERS WORKING OVER 1 HOUR".center(64, "-"))
    for entry in logs:
        time_format = "%H:%M"
        time_difference = dt.datetime.strptime(entry[2], time_format) - dt.datetime.strptime(entry[1], time_format)
        if time_difference.seconds > 60*60:
            print(f"User: {entry[0]} >> hrs worked: {time_difference}")


# 4. You are given a file called students.txt . A typical line in the file looks like: walter melon
# melon@email.msmary.edu 555-3141 There is a name, an email address, and a phone number, each separated by tabs.
# Write a program that reads through the file line-by-line, and for each line, capitalizes the first letter of the
# first and last name and adds the area code 301 to the phone number. Your program should write this to a new file
# called students2.txt . Here is what the first line of the new file should look like: Walter Melon
# melon@email.msmary.edu 301-555-3141

# Used tabs because .txt files in Pycharm are set to put 4 spaces instead of tabs
def ex4():
    with open("files/students.txt", "r") as students_file:
        students = students_file.read().splitlines()

    new_students = []

    for student in students:
        new_line = []
        line = student.split(" ")
        new_line.append(line[0].capitalize())
        new_line.append(line[1].capitalize())
        new_line.append("+48 " + line[3])
        new_line = " ".join(new_line)
        new_students.append(new_line + "\n")

    with open("files/students2.txt", "w") as new_students_file:
        new_students_file.writelines(new_students)


# 5. You are given a file namelist.txt that contains a bunch of names. Some of the names are a first name and a last
# name separated by spaces, like George Washington, while others have a middle name, like John Quincy Adams. There
# are no names consisting of just one word or more than three words. Write a program that asks the user to enter
# initials, like GW or JQA, and prints all the names that match those initials. Note that initials like JA should
# match both John Adams and John Quincy Adams.
def ex5():
    with open("files/namelist.txt", "r") as names_file:
        names = names_file.read().splitlines()
    names = [name.split() for name in names]
    query = input("Insert initials you're searching for: ").upper()
    assert 2 <= len(query) <= 3, "The initials have to contain either 2 or 3 letters"

    for name in names:
        if len(name) == 3:
            if len(query) == 3 and name[0][:1] == query[:1] and name[1][:1] == query[1:2] and name[2][:1] == query[2:]:
                print(" ".join(name))
            elif len(query) == 2 and name[0][:1] == query[:1] and name[2][:1] == query[1:]:
                print(" ".join(name))
        else:
            if name[0][:1] == query[:1] and name[1][:1] == query[:-2:-1]:
                print(" ".join(name))


# 6. You are given a file namelist.txt that contains a bunch of names. Print out all the names in the list in which
# the vowels a, e, i, o, and u appear in order (with repeats possible). The first vowel in the name must be a and
# after the first u, it is okay for there to be other vowels. An example is Ace Elvin Coulson.
def ex6():
    with open("files/namelist.txt", "r") as names_file:
        names = names_file.read().splitlines()
    regex_vowels = re.compile(r".*[Aa].*[Ee].*[Ii].*[Oo].*[Uu]")
    for name in names:
        if regex_vowels.search(name) is not None:
            print(name)


# 7. You are given a file called baseball.txt . A typical line of the file starts like below.
# Ichiro Suzuki SEA 162 680 74 ...[more stats]
# Each entry is separated by a tab, \t . The first entry is the player’s name and the second
# is their team. Following that are 16 statistics. Home runs are the seventh stat and stolen bases are the eleventh.
# Print out all the players who have at least 20 home runs and at least 20 stolen bases.
def ex7():
    with open("files/baseball.txt", "r") as baseball_file:
        players = baseball_file.readlines()
    players = [player.split(" ") for player in players]
    for player in players:
        if int(player[9]) >= 20 and int(player[13]) >= 20:
            print(" ".join(player))


# 10. Wordplay – Use the file wordlist.txt for this problem. Find the following:
# (o) All words that contain ab in multiple places, like habitable
# (p) All words with four or more vowels in a row
# (q) All words that contain both a z and a w
# (r) All words whose first letter is a, third letter is e and fifth letter is i
# (s) All two-letter words
# (t) All four-letter words that start and end with the same letter
# (u) All words that contain at least nine vowels.
# (v) All words that contain each of the letters a, b, c, d, e, and f in any order. There may be other letters in the
#     word. Two examples are backfield and feedback.
# (w) All words whose first four and last four letters are the same
# (x) All words of the form abcd*dcba, where * is arbitrarily long sequence of letters.
# (y) All groups of 5 words, like pat pet pit pot put, where each word is 3 letters, all words share the same first
#     and last letters, and the middle letter runs through all 5 vowels.
# (z) The word that has the most i’s.


def read_words():
    with open("files/wordlist.txt", "r") as words_file:
        words = words_file.read().split()
    return words


words = read_words()


# (a) All words ending in ime
def ex10a():
    for word in words:
        if word.endswith("ime"):
            print(word)


# (b) All words whose second, third, and fourth letters are ave
def ex10b():
    ave_regex = re.compile(r"\A\wave\w*")
    for word in words:
        if ave_regex.search(word) is not None:
            print(word)


# (c) How many words contain at least one of the letters r, s, t, l, n, e
# (d) The percentage of words that contain at least one of the letters r, s, t, l, n, e
def ex10cd():
    ave_regex = re.compile(r"\w*[rstlne]\w*")
    counter = 0
    for word in words:
        if ave_regex.search(word) is not None:
            counter += 1
    print(f"Number of words containing [rstlne]: {counter}\n Percentage: {counter/len(words) * 100}%")


# (e) All words with no vowels
def ex10e():
    ave_regex = re.compile(r"\w*[oaeiuy]\w*")
    for word in words:
        if ave_regex.search(word) is None:
            print(word)


# (f) All words that contain every vowel
def contains_all_vowels(string):
    vowels = ["o", "a", "e", "i", "u", "y"]
    for vowel in vowels:
        if string.find(vowel) == -1:
            return False

    return True


def ex10f():
    for word in words:
        if contains_all_vowels(word):
            print(word)


# (g) Whether there are more ten-letter words or seven-letter words
def ex10g():
    count_sevens, count_tens = 0, 0

    for word in words:
        if len(word) == 7:
            count_sevens += 1
        elif len(word) == 10:
            count_tens += 1

    if count_sevens >= count_tens:
        print(f"There are more seven-letter words. {count_sevens} to be exact.")
    else:
        print(f"There are more ten-letter words. {count_tens} to be exact.")


# (h) The longest word in the list
def ex10h():
    print(f"Longest word: {max(words, key=len)}")


# (i) All palindromes
def ex10i():
    for word in words:
        if list(word) == list(reversed(word)):
            print(word)


# (j) All words that are words in reverse, like rat and tar.
def ex10j():
    for word in words:
        reversed_word = "".join(list(reversed(word)))
        if reversed_word in words:
            print(word)


# (k) Same as above, but only print one word out of each pair.
def ex10k():
    custom_words = words
    for word in custom_words:
        reversed_word = "".join(list(reversed(word)))
        if reversed_word in custom_words:
            print(word)
            custom_words.remove(word)


# (l) All words that contain double letters next each other like aardvark or book, excluding words that end in lly
def ex10l():
    for word in words:
        word = list(word)  # TODO: figure why we need that part here. we shouldn't. and I'm sleepy.
        for i in range(len(word) - 1):
            if word[i] == word[i + 1]:
                print("".join(word))
                break


# (m) All words that contain a q that isn’t followed by a u
def ex10m():
    for word in words:
        for i in range(len(word)):
            if word[i] == "q" and word[i + 1] != "u":
                print(word)


# (n) All words that contain zu anywhere in the word
def ex10n():
    for word in words:
        if word.index("zu"):
            print(word)


ex10n()
