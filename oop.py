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
# class Cat:
#     species = 'mammal'
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# # 1 Instantiate the Cat object with 3 cats
# cat1 = Cat('Tom', 5)
# cat2 = Cat('Jerry', 4)
# cat3 = Cat('Sally', 3)
#
#
# # 2 Create a function that finds the oldest cat
# def find_oldest_cat(*cats):
#     return max(cat.age for cat in cats)
#
#
# # 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
# print(f'The oldest cat is {find_oldest_cat(cat1, cat2, cat3)} years old.')

# another cat exercise
#
# class Pets():
#     animals = []
#
#     def __init__(self, animals):
#         self.animals = animals
#
#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())
#
#
# class Cat():
#     is_lazy = True
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def walk(self):
#         return f'{self.name} is just walking around'
#
#
# class Simon(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
#
#
# class Sally(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
#
#
# #1 Add another Cat
#
# class Tikachu(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
#
#
# #2 Create a list of all of the pets (create 3 cat instances from the above)
# my_cats = []
# cat1 = Simon('Simon', 10)
# cat2 = Sally('Sally', 15)
# cat3 = Tikachu('Tikachu', 5)
#
# my_cats.append(cat1)
# my_cats.append(cat2)
# my_cats.append(cat3)
#
# #OR my_cats = [Simon('Simon', 10), Sally('Sally', 15), Tikachu('Tikachu', 5)]
#
# #3 Instantiate the Pet class with all your cats use variable my_pets
#
# my_pets = Pets(my_cats)
#
# #4 Output all of the cats walking using the my_pets instance
#
# my_pets.walk()


from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']


def capitalize(name):
    return name.capitalize()


print(list(map(capitalize, my_pets)))

#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]

print(list(zip(my_strings, sorted(my_numbers))))

#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


def filter_scores(score):
    return score > 50


print(list(filter(filter_scores, scores)))

#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
list2 = scores + my_numbers
print(list2)


def sum_numbers(acc, number):
    return acc + number


print(reduce(sum_numbers, list2, 0))
