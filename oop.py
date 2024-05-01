# OOP

# class PlayerCharacter:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def run(self):
#         print('run')
#
#
# player1 = PlayerCharacter('Tom')
# print(player1.name)
# player1.run()


#Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('Tom', 5)
cat2 = Cat('Jerry', 4)
cat3 = Cat('Sally', 3)


# 2 Create a function that finds the oldest cat
def find_oldest_cat(*cats):
    return max(cat.age for cat in cats)


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f'The oldest cat is {find_oldest_cat(cat1, cat2, cat3)} years old.')
