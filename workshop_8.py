# 2. Write a class called Product . The class should have fields called name , amount , and price , holding the
# product’s name, the number of items of that product in stock, and the regular price of the product. There should be
# a method get_price that receives the number of items to be bought and returns a the cost of buying that many items,
# where the regular price is charged for orders of less than 10 items, a 10% discount is applied for orders of
# between 10 and 99 items, and a 20% discount is applied for orders of 100 or more items. There should also be a
# method called make_purchase that receives the number of items to be bought and decreases amount by that much.

# 3. Write a class called Password_manager . The class should have a list called old_passwords that holds all of the
# user’s past passwords. The last item of the list is the user’s current password. There should be a method called
# get_password that returns the current password and a method called set_password that sets the user’s password. The
# set_password method should only change the password if the attempted password is different from all the user’s past
# passwords. Finally, create a method called is_correct that receives a string and returns a boolean True or False
# depending on whether the string is equal to the current password or not.

# 4. Write a class called Time whose only field is a time in seconds. It should have a method called
# convert_to_minutes that returns a string of minutes and seconds formatted as in the following example: if seconds
# is 230, the method should return ' 5:50 ' . It should also have a method called convert_to_hours that returns a
# string of hours, minutes, and seconds formatted analogously to the previous method.

# 5. Write a class called Converter . The user will pass a length and a unit when declaring an object from the
# class—for example, c = Converter(9, ' inches ' ) . The possible units are inches, feet, yards, miles, kilometers,
# meters, centimeters, and millimeters. For each of these units there should be a method that returns the length
# converted into those units. For example, using the Converter object created above, the user could call c.feet() and
# should get 0.75 as the result.
