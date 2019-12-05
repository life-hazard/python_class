# Text Files

# 1 You are given a file called class_scores.txt , where each line of the file contains a one-word username and a test
# score separated by spaces, like below:.
#  GWashington 83JAdams 86HWells 88
# Write code that scans through the file, adds 5 points to each test score, and outputs the user-
# names and new test scores to a new file, scores2.txt .

def ex1():
    with open("class_scores.txt", "r") as class_scores:
        print("This is a file name: ", class_scores.name)
        class_scores_contents = class_scores.readlines()
        print(class_scores_contents)
        class_scores_contents.insert(1, "KColumbus 90\n")

    with open("class_scores.txt", "w") as class_scores:
        print(class_scores_contents)
        class_scores_contents_previous = "".join(class_scores_contents)
        print(class_scores_contents_previous)
        # class_scores.write(class_scores_contents_previous)

    with open("class_scores.txt", "r") as class_scores:
        for line in class_scores:
            print(line)


def ex1_1():
    new_data = []
    with open("class_scores.txt", "r") as class_scores:
        data = class_scores.readlines()
        for line in data:
            elements = line.split()
            print(elements)
            elements[1] = str(int(elements[1]) + 5)
            print(elements)
            with open("class_scores2.txt", "a") as c:
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
    with open("grades.txt", "r") as grades:
        data = grades.readlines()
        for line in data:
            elem = line.split()
            print(elem)
            if (int(elem[1]) > 60 and int(elem[2]) > 60 and int(elem[3]) > 60):
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
    pass

# 4. You are given a file called students.txt . A typical line in the file looks like: walter melon
# melon@email.msmary.edu 555-3141 There is a name, an email address, and a phone number, each separated by tabs.
# Write a program that reads through the file line-by-line, and for each line, capitalizes the first letter of the
# first and last name and adds the area code 301 to the phone number. Your program should write this to a new file
# called students2.txt . Here is what the first line of the new file should look like: Walter Melon
# melon@email.msmary.edu 301-555-3141

# 5. You are given a file namelist.txt that contains a bunch of names. Some of the names are a first name and a last
# name separated by spaces, like George Washington, while others have a middle name, like John Quincy Adams. There
# are no names consisting of just one word or more than three words. Write a program that asks the user to enter
# initials, like GW or JQA, and prints all the names that match those initials. Note that initials like JA should
# match both John Adams and John Quincy Adams.

# 6. You are given a file namelist.txt that contains a bunch of names. Print out all the names in the list in which
# the vowels a, e, i, o, and u appear in order (with repeats possible). The first vowel in the name must be a and
# after the first u, it is okay for there to be other vowels. An example is Ace Elvin Coulson.

# 7. You are given a file called baseball.txt . A typical line of the file starts like below. Ichiro Suzuki SEA 162
# 680 74 ...[more stats] Each entry is separated by a tab, \t . The first entry is the player’s name and the second
# is their team. Following that are 16 statistics. Home runs are the seventh stat and stolen bases are the eleventh.
# Print out all the players who have at least 20 home runs and at least 20 stolen bases.

# 10. Wordplay – Use the file wordlist.txt for this problem. Find the following:
# (a) All words ending in ime
# (b) All words whose second, third, and fourth letters are ave
# (c) How many words contain at least one of the letters r, s, t, l, n, e
# (d) The percentage of words that contain at least one of the letters r, s, t, l, n, e
# (e) All words with no vowels
# (f) All words that contain every vowel
# (g) Whether there are more ten-letter words or seven-letter words
# (h) The longest word in the list
# (i) All palindromes
# (j) All words that are words in reverse, like rat and tar.
# (k) Same as above, but only print one word out of each pair.
# (l) All words that contain double letters next each other like aardvark or book, excluding words that end in lly
# (m) All words that contain a q that isn’t followed by a u
# (n) All words that contain zu anywhere in the word
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
