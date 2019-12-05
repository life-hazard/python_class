# 1. Write a program that asks the user to enter a list of integers. Do the following:
# (a) Print the total number of items in the list.
# (b) Print the last item in the list.
# (c) Print the list in reverse order.
# (d) Print Yes if the list contains a 5 and No otherwise.
# (e) Print the number of fives in the list.
# (f) Remove the first and last items from the list, sort the remaining items
# (g) Print how many integers in the list are less than 5.

def list_of_integers():
    int_list = []
    print("Enter integers separated by enter, to stop leave blank.")
    while (True):
        # print("Enter integers separated by enter, to stop press q.")
        new_elem = input()
        if new_elem == '':
            break
        int_list.append(new_elem)
    print(int_list)

    # (a) Print the total number of items in the list.

    print("The number of elements in your list: ", len(int_list))

    # (b) Print the last item in the list.

    print("The last item in the list: ", int_list[-1])

    # (c) Print the list in reverse order.

    int_list.reverse()
    print("The list in reverse order: ", int_list)

    # (d) Print Yes if the list contains a 5 and No otherwise.

    if '5' in int_list:
        print("There is a 5 in list")
    else:
        print("There is no 5 in list")

    # (e) Print the number of fives in the list.

    print("There are", int_list.count('5'), "fives in list.")

    # (f) Remove the first and last items from the list, sort the remaining items

    int_list.pop(0)
    int_list.pop(-1)
    int_list.sort()
    print("Sorted list without first and last elements: ", int_list)

    # (g) Print how many integers in the list are less than 5.
    counter = 0
    for i in range(len(int_list)):
        if int(int_list[i]) < 5:
            counter += 1
    print("There are", counter, "integers less then 5 ")


# 4. Ask the user to enter a list containing numbers between 1 and 12. Then replace all of the entries in the list
# that are greater than 10 with 10.

def changing_tens():
    print("Enter numbers between 1 and 12. To finish enter nothing")
    elements = []
    while (True):
        new_elem = input()
        if new_elem == '':
            break
        elements.append(new_elem)
    print(elements)

    for i in range(len(elements)):
        if int(elements[i]) > 10:
            elements[i] = '10'
    print(elements)


# 10. Write a program that rotates the elements of a list so that the element at the first index moves to the second index, the element in the second index moves to the third index, etc., and the element in the last index moves to the first index.

import random


def ten():
    unrotated = [1, 2, 5, 5, 5]
    rotated = []
    for i in reversed(unrotated):
        rotated.append(i)
    print(rotated)


# 11. Using a for loop, create the list below, which consists of ones separated by increasingly many zeroes.
# The last two ones in the list should be separated by ten zeroes. [1,1,0,1,0,0,1,0,0,0,1,0,0,0,0,1,....]

def eleven():
    list_a = []
    for i in range(11):
        list_a.append(1)
        for j in range(i):
            list_a.append(0)
    list_a.append(1)
    print(list_a)


# 12. Write a program that generates 100 random integers that are either 0 or 1.
# Then find the longest run of zeros, the largest number of zeros in a row.
# For instance, the longest run of zeros in [1,0,1,1,0,0,0,0,1,0,0] is 4.

def twelve():
    list_a = []
    counter = 0
    counter_list = []
    for i in range(100):
        list_a.append(random.randint(0, 1))
        if list_a[i] == 0:
            counter += 1
            counter_list.append(counter)
        if list_a[i] == 1 and i < (100 - counter):
            counter = 0
    # print(list_a)
    print("Couter:", max(counter_list))


# 13. Write a program that removes any repeated items from a list so that each item appears at most once. F
# or instance, the list [1,1,2,3,4,3,0,0] would become [1,2,3,4,0] .

def remove_repeated():
    print("Enter elements. To finish enter nothing")
    new_list = []
    while (True):
        new_elem = input()
        if new_elem == '':
            break
        new_list.append(new_elem)
    print(new_list)

    new_list.sort()
    end = len(new_list) - 1
    for i in range(end, 0, -1):
        if new_list[i - 1] == new_list[i]:
            new_list.pop(i - 1)
        else:
            temp = new_list[i - 1]
    print(new_list)


# 14. Write a program that asks the user to enter a length in feet. The program should then give the user the option
# to convert from feet into inches, yards, miles, millimeters, centimeters, meters, or kilometers.
# Say if the user enters a 1 , then the program converts to inches, if they enter a 2 , then the program converts
# to yards, etc. While this can be done with if statements, it is much shorter with lists and it is also easier
# to add new conversions if you use lists.

def feet_conversion():
    feet = input("Feet: ")
    # inch yards miles millimeters cm m km
    converting = [12, 0.33333, 0.0001893939, 304.8, 30.48, 0.3048, 0.0003048]
    unit = input("Feet to inch(1), yards(2), miles(3), millimeters(4), centimeters(5), meters(6), kilometers(7) ")
    print(feet, " = ", int(converting[int(unit) - 1]) * int(feet))


# 15. There is a provably unbreakable cipher called a one-time pad. The way it works is you shift each character
# of the message by a random amount between 1 and 26 characters, wrapping around the alphabet if necessary.
# For instance, if the current character is y and the shift is 5, then the new character is d.
# Each character gets its own shift, so there needs to be as many random shifts as there are characters in the message.
# As an example, suppose the user enters secret. The program should generate a random shift between 1 and 26
# for each character. Suppose the randomly generated shifts are 1, 3, 2, 10, 8, and 2.
# The encrypted message wouldbe thebmv.
# (a) Write a program that asks the user for a message and encrypts the message using the one-time pad.
# First convert the string to lowercase. Any spaces and punctuation in the string should be left unchanged.
# For example, Secret!!! becomes thebmv!!! using the shifts above.
# (b) Write a program to decrypt a string encrypted as above. The reason it is called a one-time-pad is that
# the list of random shifts should only be used once. It becomes easily breakable if the same random shifts are used
# for more than one message. Moreover, it is only provably unbreakable if the random numbers are truly random,
# and the numbers generated by randint are not truly random. For this problem, just use randint ,
# but for cryptographically safe random numbers, see Section 22.8.Chapter 8


def cipher():
    message = input("Message: ")
    message = message.lower()
    key = []
    encrypted_message = []
    # encryption
    for i in message:
        shift = random.randint(1, 26)
        key.append(shift)
        # print(i)
        if ord(i) == 32:
            i = chr(ord(i))
        else:
            i = chr(ord(i) + shift)
            if ord(i) > 122:
                i = chr(ord(i) - 25)
        # print(i)
        encrypted_message.append(i)
        en_message = ''.join(encrypted_message)
    print(key)
    print(en_message)
    # decryption
    decrypted_message = []
    j = 0
    for i in encrypted_message:
        shift = key[j]
        if ord(i) == 32:
            i = chr(ord(i))
        else:
            i = chr(ord(i) - shift)
            if ord(i) < 97:
                i = chr(ord(i) + 25)
        j += 1
        decrypted_message.append(i)
        dec_message = ''.join(decrypted_message)
    print(dec_message)
