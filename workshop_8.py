# 2. Write a class called Product . The class should have fields called name , amount , and price , holding the
# product’s name, the number of items of that product in stock, and the regular price of the product. There should be
# a method get_price that receives the number of items to be bought and returns a the cost of buying that many items,
# where the regular price is charged for orders of less than 10 items, a 10% discount is applied for orders of
# between 10 and 99 items, and a 20% discount is applied for orders of 100 or more items. There should also be a
# method called make_purchase that receives the number of items to be bought and decreases amount by that much.


class Product:
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price

    def get_price(self, number):
        if number <= self.amount:
            if number < 10:
                bill = number * self.price
                print('The cost: ', bill)
            if 10 <= number <= 99:
                bill = number * self.price
                print('The cost: ', bill * 0.9)
            if number >= 100:
                bill = number * self.price
                print('The cost: ', bill * 0.8)
        else:
            print('There\'s not enough items in stock')

    def make_purchase(self, number):
        if number <= self.amount:
            self.get_price(number)
            self.amount = self.amount - number
        else:
            print('There\'s not enough items in stock')


# 3. Write a class called Password_manager . The class should have a list called old_passwords that holds all of the
# user’s past passwords. The last item of the list is the user’s current password. There should be a method called
# get_password that returns the current password and a method called set_password that sets the user’s password. The
# set_password method should only change the password if the attempted password is different from all the user’s past
# passwords. Finally, create a method called is_correct that receives a string and returns a boolean True or False
# depending on whether the string is equal to the current password or not.


class PasswordManager:
    def __init__(self, old_passwords):
        self.old_passwords = old_passwords

    def get_password(self):
        current = self.old_passwords[-1]
        print(current)

    def set_password(self, new_password):
        self.old_passwords.append(new_password)

    def is_correct(self, entered_password):
        print(entered_password)
        print(self.get_password())
        if entered_password == self.old_passwords[-1]:
            return True
        else:
            return False


# 4. Write a class called Time whose only field is a time in seconds. It should have a method called
# convert_to_minutes that returns a string of minutes and seconds formatted as in the following example: if seconds
# is 230, the method should return ' 3:50 ' . It should also have a method called convert_to_hours that returns a
# string of hours, minutes, and seconds formatted analogously to the previous method.


class Time:
    def __init__(self, seconds):
        self.seconds = seconds

    def convert_to_minutes(self):
        minute = 0
        time = self.seconds

        for i in range(1, time + 1):
            if i % 60 == 0:
                minute += 1
        second = time - minute * 60

        print(str(minute), ':', str(second))

    def convert_to_hours(self):
        hour = 0
        minute = 0
        time = self.seconds

        for i in range(1, time + 1):
            if i % 3600 == 0:
                hour += 1

        time_left = time - hour * 3600

        for i in range(1, time_left + 1):
            if i % 60 == 0:
                minute += 1
        second = time_left - minute * 60

        print(str(hour), ':', str(minute), ':', str(second))


# 5. Write a class called Converter . The user will pass a length and a unit when declaring an object from the
# class—for example, c = Converter(9, ' inches ' ) . The possible units are inches, feet, yards, miles, kilometers,
# meters, centimeters, and millimeters. For each of these units there should be a method that returns the length
# converted into those units. For example, using the Converter object created above, the user could call c.feet() and
# should get 0.75 as the result.


class Converter:
    def __init__(self, length, unit):
        self.length = length
        self.unit = unit

    # inches, feet, yards, miles, kilometers, meters, centimeters, and millimeters
    def inches(self):
        if self.unit == 'in':
            print(self.length, self.unit, ' = ', self.length, 'in')
        if self.unit == 'ft':
            print(self.length, self.unit, ' = ', self.length * 12, 'in')
        if self.unit == 'yd':
            print(self.length, self.unit, ' = ', self.length * 36, 'in')
        if self.unit == 'mi':
            print(self.length, self.unit, ' = ', round(self.length * 63360.23622, 2), 'in')
        if self.unit == 'km':
            print(self.length, self.unit, ' = ', round(self.length * 39370.07874, 2), 'in')
        if self.unit == 'm':
            print(self.length, self.unit, ' = ', round(self.length * 39.37007874, 2), 'in')
        if self.unit == 'cm':
            print(self.length, self.unit, ' = ', round(self.length * 0.3937007874, 2), 'in')
        if self.unit == 'mm':
            print(self.length, self.unit, ' = ', round(self.length * 0.0393700787, 2), 'in')

    def feet(self):
        if self.unit == 'in':
            print(self.length, self.unit, ' = ', round(self.length * 0.0833333333, 2), 'ft')
        if self.unit == 'ft':
            print(self.length, self.unit, ' = ', self.length, 'ft')
        if self.unit == 'yd':
            print(self.length, self.unit, ' = ', self.length * 3, 'ft')
        if self.unit == 'mi':
            print(self.length, self.unit, ' = ', round(self.length * 5280.019685, 2), 'ft')
        if self.unit == 'km':
            print(self.length, self.unit, ' = ', round(self.length * 3280.839895, 2), 'ft')
        if self.unit == 'm':
            print(self.length, self.unit, ' = ', round(self.length * 3.280839895, 2), 'ft')
        if self.unit == 'cm':
            print(self.length, self.unit, ' = ', round(self.length * 0.032808399, 2), 'ft')
        if self.unit == 'mm':
            print(self.length, self.unit, ' = ', round(self.length * 0.0032808399, 3), 'ft')

    def yards(self):
        if self.unit == 'in':
            print(self.length, self.unit, ' = ', round(self.length * 0.0277777778, 2), 'yd')
        if self.unit == 'ft':
            print(self.length, self.unit, ' = ', round(self.length * 0.3333333333, 2), 'yd')
        if self.unit == 'yd':
            print(self.length, self.unit, ' = ', self.length, 'yd')
        if self.unit == 'mi':
            print(self.length, self.unit, ' = ', round(self.length * 1760.0065617, 2), 'yd')
        if self.unit == 'km':
            print(self.length, self.unit, ' = ', round(self.length * 1093.6132983, 2), 'yd')
        if self.unit == 'm':
            print(self.length, self.unit, ' = ', round(self.length * 1.0936132983, 2), 'yd')
        if self.unit == 'cm':
            print(self.length, self.unit, ' = ', round(self.length * 0.010936133, 3), 'yd')
        if self.unit == 'mm':
            print(self.length, self.unit, ' = ', round(self.length * 0.001093613, 4), 'yd')

    def miles(self):
        if self.unit == 'in':
            print(self.length, self.unit, ' = ', round(self.length * 0.0000157828, 6), 'mi')
        if self.unit == 'ft':
            print(self.length, self.unit, ' = ', round(self.length * 0.0001893932, 6), 'mi')
        if self.unit == 'yd':
            print(self.length, self.unit, ' = ', round(self.length * 0.0005681797, 6), 'mi')
        if self.unit == 'mi':
            print(self.length, self.unit, ' = ', self.length, 'mi')
        if self.unit == 'km':
            print(self.length, self.unit, ' = ', round(self.length * 0.6213688756, 2), 'mi')
        if self.unit == 'm':
            print(self.length, self.unit, ' = ', round(self.length * 0.0006213689, 5), 'mi')
        if self.unit == 'cm':
            print(self.length, self.unit, ' = ', round(self.length * 0.0000062137, 7), 'mi')
        if self.unit == 'mm':
            print(self.length, self.unit, ' = ', round(self.length * 0.0000006213689, 9), 'mi')

    def kilometers(self):
        if self.unit == 'in':
            print(self.length, self.unit, ' = ', round(self.length * 0.0000254, 6), 'km')
        if self.unit == 'ft':
            print(self.length, self.unit, ' = ', round(self.length * 0.0003048, 5), 'km')
        if self.unit == 'yd':
            print(self.length, self.unit, ' = ', round(self.length * 0.0009144, 5), 'km')
        if self.unit == 'mi':
            print(self.length, self.unit, ' = ', round(self.length * 1.60935, 2), 'km')
        if self.unit == 'km':
            print(self.length, self.unit, ' = ', self.length, 'km')
        if self.unit == 'm':
            print(self.length, self.unit, ' = ', round(self.length * 0.001, 3), 'km')
        if self.unit == 'cm':
            print(self.length, self.unit, ' = ', round(self.length * 0.00001, 5), 'km')
        if self.unit == 'mm':
            print(self.length, self.unit, ' = ', round(self.length * 0.000001, 6), 'km')

    def meters(self):
        if self.unit == 'in':
            print(self.length, self.unit, ' = ', round(self.length * 0.0254, 3), 'm')
        if self.unit == 'ft':
            print(self.length, self.unit, ' = ', round(self.length * 0.3048, 2), 'm')
        if self.unit == 'yd':
            print(self.length, self.unit, ' = ', round(self.length * 0.9144, 2), 'm')
        if self.unit == 'mi':
            print(self.length, self.unit, ' = ', round(self.length * 1609.35, 2), 'm')
        if self.unit == 'km':
            print(self.length, self.unit, ' = ', self.length * 1000, 'm')
        if self.unit == 'm':
            print(self.length, self.unit, ' = ', self.length, 'm')
        if self.unit == 'cm':
            print(self.length, self.unit, ' = ', self.length * 0.01, 'm')
        if self.unit == 'mm':
            print(self.length, self.unit, ' = ', round(self.length * 0.001, 3), 'm')

    def centimeters(self):
        if self.unit == 'in':
            print(self.length, self.unit, ' = ', self.length * 2.54, 'cm')
        if self.unit == 'ft':
            print(self.length, self.unit, ' = ', self.length * 30.48, 'cm')
        if self.unit == 'yd':
            print(self.length, self.unit, ' = ', self.length * 91.44, 'cm')
        if self.unit == 'mi':
            print(self.length, self.unit, ' = ', self.length * 160935, 'cm')
        if self.unit == 'km':
            print(self.length, self.unit, ' = ', self.length * 100000, 'cm')
        if self.unit == 'm':
            print(self.length, self.unit, ' = ', self.length * 100, 'cm')
        if self.unit == 'cm':
            print(self.length, self.unit, ' = ', self.length, 'cm')
        if self.unit == 'mm':
            print(self.length, self.unit, ' = ', self.length * 0.1, 'cm')

    def milimeters(self):
        if self.unit == 'in':
            print(self.length, self.unit, ' = ', self.length * 25.4, 'mm')
        if self.unit == 'ft':
            print(self.length, self.unit, ' = ', self.length * 304.8, 'mm')
        if self.unit == 'yd':
            print(self.length, self.unit, ' = ', self.length * 914.4, 'mm')
        if self.unit == 'mi':
            print(self.length, self.unit, ' = ', self.length * 1609350, 'mm')
        if self.unit == 'km':
            print(self.length, self.unit, ' = ', self.length * 1000000, 'mm')
        if self.unit == 'm':
            print(self.length, self.unit, ' = ', self.length * 1000, 'mm')
        if self.unit == 'cm':
            print(self.length, self.unit, ' = ', self.length * 10, 'mm')
        if self.unit == 'mm':
            print(self.length, self.unit, ' = ', self.length, 'mm')
