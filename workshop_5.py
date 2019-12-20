import numpy as np
import random


def ex1():
    list = {}
    while (True):
        print('Adding products, to add press enter, to finish press 0.')
        if input() != '0':
            product_name = input('Enter product name: ')
            product_price = input('Enter product price: ')
            if product_name in list:
                print('The previous price has been updated.')
            list[product_name] = product_price

        else:
            print('Your list of products:  ', list)
            break

    dollar = input('Enter amount: ')
    print('Showing the products with lesser prices')
    for product_name in list:
        if list[product_name] <= dollar:
            print(product_name, ' : ', list[product_name])


# 3. For this problem, use the dictionary from the beginning of this chapter whose keys are month names
# and whose values are the number of days in the corresponding months.
# (a) Ask the user to enter a month name and use the dictionary to tell them how many days are in the month.
# (b) Print out all of the keys in alphabetical order.
# (c) Print out all of the months with 31 days.
# (d) Print out the (key-value) pairs sorted by the number of days in each month
# (e) Modify the program from part (a) and the dictionary so that the user does not have to know
# how to spell the month name exactly. That is, all they have to do is spell the first three letters of the month
# name correctly.

def ex3():
    days = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31,
            'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31, 'Jan': 31, 'Feb': 28,
            'Mar': 31, 'Apr': 30, 'May': 31, 'Jun': 30, 'Jul': 31, 'Aug': 31, 'Sep': 30, 'Oct': 31, 'Nov': 30,
            'Dec': 31}
    asked = input('Which month would you like? ')
    if asked not in days:
        print('There\'s no such month')
    else:
        print(asked, ' has ', days[asked], ' days.')

    for i in sorted(days):
        print(i, ' ', days[i])

    print('Months with 31 days')
    for i in days:
        if days[i] == 31:
            print(i, ' ')

    print('Months sorted by number of days')
    for i in sorted(days, key=days.get):
        print(days[i], ' - ', i)

    ask = input('Which month would you like? ')
    asked = str(ask[:3])
    if asked not in days:
        print('There\'s no such month')
    else:
        print(asked, ' has ', days[asked], ' days.')


# 4. Write a program that uses a dictionary that contains ten user names and passwords.
# The program should ask the user to enter their username and password.
# If the username is not in the dictionary, the program should indicate that the person
# is not a valid user of the system. If the username is in the dictionary, but the user does not enter the right
# password, the program should say that the password is invalid. If the password is correct,
# then the program should tell the user that they are now logged in to the system.

def ex4():
    logs = {}
    for i in range(10):
        login = input("Login: ")
        password = input("Password: ")
        logs[login] = password
    print(logs)
    print("Enter correct login and password")
    your_login = input("Login: ")
    if your_login in logs:
        your_password = input("Password: ")
        if your_password == logs[your_login]:
            print("You\'ve been successfully logged in!")
        else:
            print("Wrong password!")
    else:
        print("There is no user with this login")


# 5. Repeatedly ask the user to enter a team name and the how many games the team won and how many they lost.
# Store this information in a dictionary where the keys are the team names and the values are lists of the form
# [ wins , losses ] .
# (a) Using the dictionary created above, allow the user to enter a team name and print out the team’s winning percentage.
# (b) Using the dictionary, create a list whose entries are the number of wins of each team.
# (c) Using the dictionary, create a list of all those teams that have winning records.

def ex5():
    base = {}
    games = {}
    won = "won"
    lost = "lost"
    while True:
        answer = input("Do you want to add a team? [Y/N]")
        if answer == "y":
            team_name = input("Enter Team Name: ")
            wins = input("Games won: ")
            games[won] = wins
            loses = input("Games lost: ")
            games[lost] = loses
            # base[team_name] = games[won], games[lost]
            base[team_name] = wins, loses
        if answer == "n":
            break
    print(base)
    searching_team_percentage = input("Show winning stats of: ")
    if searching_team_percentage in base:
        team_percentage = int(base[searching_team_percentage][0]) / (int(base[searching_team_percentage][0])
                                                                     + int(base[searching_team_percentage][1]))
        print(team_percentage)
    else:
        print("There\'s no such team")


# 6. Repeatedly ask the user to enter game scores in a format like team1 score1 - team2 score2.
# Store this information in a dictionary where the keys are the team names and the values are lists
# of the form [ wins , losses ] .

# team1 [1, 0]

"""
    FIX LATER !
"""


def ex6():
    scores = []
    team_scores = {}
    wins1 = 0
    loses1 = 0
    wins2 = 0
    loses2 = 0
    while True:
        answer = input("Do you want to add game scores? [Y/N]")
        if answer == "y":
            score_line = input("Enter game scores: team score - team score")
            score_line = score_line.replace('-', '')
            score_line = score_line.split()
            team_1 = score_line[0]
            team_2 = score_line[2]
            score_1 = score_line[1]
            score_2 = score_line[3]
            if team_1 or team_2 in team_scores:
                # if score_1 > score_2:
                if score_1 > score_2:
                    # if team_1 or team_2 in team_scores:
                    team_scores[team_1][0] += 1
                    team_scores[team_2][1] += 1
                    # team_scores[team_1] = wins1, loses1
                    # team_scores[team_2] = wins2, loses2
                    print(team_scores)
                else:
                    team_scores[team_2][0] += 1
                    team_scores[team_1][1] += 1
                    # team_scores[team_2] = wins2, loses2
                    # team_scores[team_1] = wins1, loses1
                    print(team_scores)
        if answer == "n":
            break
    print(team_scores)


# 7. Create a 5 × 5 list of numbers. Then write a program that creates a dictionary whose keys are the numbers
# and whose values are the how many times the number occurs. Then print the three most common numbers.


def repeating_in_matrix():
    x = 5
    y = 5
    matrix = np.random.randint(10, size=(5, 5))
    print(matrix)


# repeating_in_matrix() TODO: I think you should finish this or something.

# 8. Using the card dictionary from earlier in this chapter, create a simple card game that deals two players three
# cards each. The player with the highest card wins. If there is a tie, then compare the second highest card and,
# if necessary, the third highest. If all three cards have the same value, then the game is a draw.
# 9. Using the card dictionary from earlier in the chapter, deal out three cards. Determine the following:
# (a) If the three cards form a flush (all of the same suit)
# (b) If there is a three-of-a-kind (all of the same value)
# (c) If there is a pair, but not three-of-a-kind
# (d) If the three cards form a straight (all in a row, like (2, 3, 4) or (10, Jack, Queen))

# BASIC EXERCISES
# 1. Write a Python program to create a set
# 2. Write a Python program to iteration over sets.
# 3. Write a Python program to add member(s) in a set
# 4. Write a Python program to remove item(s) from set
# 5. Write a Python program to remove an item from a set if it is present in the set.
# 6. Write a Python program to create an intersection of sets.
# 7. Write a Python program to create a union of sets.
# 8. Write a Python program to create set difference.
# 9. Write a Python program to create a symmetric difference.
# 10. Write a Python program to issubset and issuperset.
# 11. Write a Python program to create a shallow copy of sets.
# 12. Write a Python program to clear a set.

# EXERCISES
# 1. Given a list of integers. Determine how many distinct numbers there are. This task can be solved in one line of
# code.
distinct_int = lambda integers: sum([1 for integer in integers if integers.count(integer) == 1])

# print(distinct_int([12, 15, 15, 6, 7, 9, 9, 9, 4, 15]))  # Example

# 2. Given two lists of numbers. Count how many unique numbers occur in both of them. This task can be solved in one
# line of code.

# 3. Given two lists of numbers. Find all the numbers that occur in both the first and the second list and print them
# in ascending order. Even this task can be solved in one line of code.
# 4. Given a sequence of numbers, determine if the next number has already been encountered. For each number, print
# the word YES (in a separate line) if this number has already been encountered, and print NO, if it has not already
# been encountered.
# 5. Alice and Bob like to play with colored cubes. Each child has its own set of cubes and each cube has a distinct
# color, but they want to know how many unique colors exist if they combine their block sets. To determine this, the
# kids enumerated each distinct color with a random number from 0 to 108. At this point their enthusiasm dried up,
# and you are invited to help them finish the task. Given two integers that indicate the number of blocks in Alice's
# and then Bob's sets N and M. The following N lines contain the numerical color value for each cube in Alice's set.
# Then the last M rows contain the numberical color value for each cube in Bob's setFind three sets: the numerical
# colors of cubes in both sets, the numerical colors of cubes only in Alice's set, and the numerical colors of cubes
# only in Bob's set. For each set, print the number of elements in the set, followed by the numerical color elements,
# sorted in ascending order.
# 6. Given a number n, followed by n lines of text, print the number of distinct words that appear in the text.
# For this, we define a word to be a sequence of non-whitespace characters, seperated by one or more whitespace or
# newline characters. Punctuation marks are part of a word, in this definition.
# 7. Augustus and Beatrice play the following game. Augustus thinks of a secret integer number from 1 to n. Beatrice
# tries to guess the number by providing a set of integers. Augustus answers YES if his secret number exists in the
# provided set, or NO, if his number does not exist in the provided numbers. Then after a few questions Beatrice,
# totally confused, asks you to help her determine Augustus's secret number. Given the value of n in the first line,
# followed by the a sequence Beatrice's guesses, series of numbers seperated by spaces and Agustus's responses, or
# Beatrice's plea for HELP. When Beatrice calls for help, provide a list of all the remaining possible secret numbers,
# in ascending order, separated by a space.


# EXERCISES 1. Write a function called rectangle that takes two integers m and n as arguments and prints out an
# m × n box consisting of asterisks. Shown below is the output of rectangle(2,4)
# 2.
# (a) Write a function called add_excitement that takes a list of strings and adds an exclamation point ( ! ) to the
# end of each string in the list. The program should modify the  original list and not return anything.
# (b) Write the same function except thatit should not modify the original list and should instead return a new list.
# 3. Write a function called sum_digits that is given an integer num and returns the sum of the digits of num .
# 4. The digital root of a number n is obtained as follows: Add up the digits n to get a new number. Add up the digits
# of that to get another new number. Keep doing this until you get a number that has only one digit. That number is
# the digital root. For example, if n = 45893 , we add up the digits to get 4 + 5 + 8 + 9 + 3 = 29 . We then add up
# the digits of 29 to get 2 + 9 = 11 . We then add up the digits of 11 to get 1 + 1 = 2 . Since 2 has only one digit,
# 2 is our digital root. Write a function that returns the digital root of an integer n . [Note: there is a shortcut,
# where the digital root is equal to n mod 9, but do not use that here.]
# 5. Write a function called first_diff that is given two strings and returns the first location in which the strings
# differ. If the strings are identical, it should return -1.
# 6. Writea function called binom(n,k) that takes two integers n and k and returns the binomial coefficient.
# The definition is nk = k!(n−k)!.
# 7. Write a function that takes an integer n and returns a random integer with exactly n digits. For instance,
# if n is 3, then 125 and 593 would be valid return values, but 093 would not because that is really 93, which is
# a two-digit number.
# 8. Write a function called number_of_factors that takes an integer and returns how many factors the number has.
# 9. Write a function called factors that takes an integer and returns a list of its factors.
# 10. Write a function called closest that takes a list of numbers L and a number n and returns the largest element
# in L that is not larger than n . For instance, if L=[1,6,3,9,11] and n=8 , then the function should return 6,
# because 6 is the closest thing in L to 8 that is not larger than 8. Don’t worry about if all of the things in L
# are smaller than n .126
# 11. Write a function called matches that takes two strings as arguments and returns how many matches there are
# between the strings. A match is where the two strings have the same character at the same index. For instance,
# ' python ' and ' path ' match in the first, third, and fourth characters, so the function should return 3.
# 12. Recall that if s is a string, then s.find( ' a ' ) will find the location of the first a in s. The problem is
# that it does not find the location of every a. Write a function called findall that given a string and a single
# character, returns a list containing all of the locations of that character in the string. It should return an
# empty list if there are no occurrences of the character in the string.
# 13. Write a function called change_case that given a string, returns a string with each upper case letter replaced
# by a lower case letter and vice-versa.
# 14. Write a function called is_sorted that is given a list and returns True if the list is sorted and False
# otherwise.
# 15. Write a function called root that is given a number x and an integer n and returns x 1/n . In the function
# definition, set the default value of n to 2.
# 16. Write a function called one_away that takes two strings and returns True if the strings are of the same length
# and differ in exactly one letter, like bike/hike or water/wafer.
# 17.
# (a) Write a function called primes that is given a number n and returns a list of the first n primes. Let the
# default value of n be 100.
# (b) Modify the function above so that there is an optional argument called start that allows the list to start at
# a value other than 2. The function should return the first n primes that are greater than or equal to start.
# The default value of start should be 2.
