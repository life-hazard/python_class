
def ex1():
    list = {}
    while(True):
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

#3. For this problem, use the dictionary from the beginning of this chapter whose keys are month names
# and whose values are the number of days in the corresponding months.
 #(a) Ask the user to enter a month name and use the dictionary to tell them how many days are in the month.
 #(b) Print out all of the keys in alphabetical order.
 #(c) Print out all of the months with 31 days.
 #(d) Print out the (key-value) pairs sorted by the number of days in each month
 #(e) Modify the program from part (a) and the dictionary so that the user does not have to know
# how to spell the month name exactly. That is, all they have to do is spell the first three letters of the month name correctly.

def ex3():
    days = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31,
            'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31, 'Jan': 31, 'Feb': 28,
            'Mar': 31, 'Apr': 30, 'May': 31, 'Jun': 30, 'Jul': 31, 'Aug': 31, 'Sep': 30, 'Oct': 31, 'Nov': 30, 'Dec': 31}
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

#4. Write a program that uses a dictionary that contains ten user names and passwords.
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

#5. Repeatedly ask the user to enter a team name and the how many games the team won and how many they lost.
# Store this information in a dictionary where the keys are the team names and the values are lists of the form
# [ wins , losses ] .
 #(a) Using the dictionary created above, allow the user to enter a team name and print out the team’s winning percentage.
 #(b) Using the dictionary, create a list whose entries are the number of wins of each team.
 #(c) Using the dictionary, create a list of all those teams that have winning records.

def ex5() :
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
            #base[team_name] = games[won], games[lost]
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

#6. Repeatedly ask the user to enter game scores in a format like team1 score1 - team2 score2.
# Store this information in a dictionary where the keys are the team names and the values are lists
# of the form [ wins , losses ] .

def ex6():
    scores = []
    team_scores = {}
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
            if score_1 > score_2:
                # DOKONCZYC
                if team_1 in team_scores:
                    team_scores[team_1] = int(team_scores[team_1]) + int(score_1)
                else:
                    team_scores = team_1
                    team_scores[team_1] = score_1

        if answer == "n":
            break
    print(team_scores)

ex6()