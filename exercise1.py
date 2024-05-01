# from datetime import datetime
# age = int(datetime.now().year) - int(input('what is your year birth? '))
# print("you are " + str(age) + " years old")
#

# enumerate

for i, j in enumerate(['a', 'b', 'c']):
    print(i, j)

for i, j in enumerate(list(range(100))):
    if j == 50:
        print(i, j)
