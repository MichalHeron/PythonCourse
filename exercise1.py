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
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []

for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)