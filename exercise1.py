# from datetime import datetime
# age = int(datetime.now().year) - int(input('what is your year birth? '))
# print("you are " + str(age) + " years old")
#

# enumerate

# for i, j in enumerate(['a', 'b', 'c']):
#     print(i, j)
#
# for i, j in enumerate(list(range(100))):
#     if j == 50:
#         print(i, j)

#Exercise!
#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
# picture = [
#     [0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 1, 1, 1, 0, 0],
#     [0, 1, 1, 1, 1, 1, 0],
#     [1, 1, 1, 1, 1, 1, 1],
#     [0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 0, 1, 0, 0, 0]
# ]
#
# for i in picture:
#     for pixel in i:
#         if pixel:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()

# Exercise: Check for duplicates in list:
# some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
#
# duplicates = []
#
# for value in some_list:
#     if some_list.count(value) > 1:
#         if value not in duplicates:
#             duplicates.append(value)
#
# print(duplicates)

# tesla exercise

# age_input = input("What is your age?: ")
#
#
# def check_driver_age(age="0"):
#     '''
#     This function will take an age as an input and tell you if you are too young to drive this car.
#     '''
#     if int(age) < 18:
#         print("Sorry, you are too young to drive this car. Powering off")
#     elif int(age) > 18:
#         print("Powering On. Enjoy the ride!")
#     elif int(age) == 18:
#         print("Congratulations on your first year of driving. Enjoy the ride!")
#
#
# check_driver_age(age_input)
#
# print(check_driver_age.__doc__)
#1. Wrap the above code in a function called checkDriverAge(). Whenever you call this function, you will get prompted for age.
# Notice the benefit in having checkDriverAge() instead of copying and pasting the function everytime?

#2 Instead of using the input(). Now, make the checkDriverAge() function accept an argument of age, so that if you enter:
#checkDriverAge(92);
#it returns "Powering On. Enjoy the ride!"
#also make it so that the default age is set to 0 if no argument is given.

# highest even exercise

def highest_even(li):
    """
    A function that takes a list of numbers, filters out the odd numbers, and returns the highest even number in the list.

    Parameters:
    li (list): A list of integers.

    Returns:
    int: The highest even number in the input list.
    """
    even_list = []
    for element in li:
        if element % 2 == 0:
            even_list.append(element)
    return max(even_list)


print(highest_even([10, 2, 3, 4, 8, 11, 20]))
