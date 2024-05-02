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

#
# from functools import reduce
#
# #1 Capitalize all of the pet names and print the list
# my_pets = ['sisi', 'bibi', 'titi', 'carla']
#
#
# def capitalize(name):
#     return name.capitalize()
#
#
# print(list(map(capitalize, my_pets)))
#
# #2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
# my_strings = ['a', 'b', 'c', 'd', 'e']
# my_numbers = [5, 4, 3, 2, 1]
#
# print(list(zip(my_strings, sorted(my_numbers))))
#
# #3 Filter the scores that pass over 50%
# scores = [73, 20, 65, 19, 76, 100, 88]
#
#
# def filter_scores(score):
#     return score > 50
#
#
# print(list(filter(filter_scores, scores)))
#
# #4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
# list2 = scores + my_numbers
# print(list2)
#
#
# def sum_numbers(acc, number):
#     return acc + number
#
#
# print(reduce(sum_numbers, list2, 0))


##### square using lambda
#
# my_list = [5, 4, 3]
#
#
# print(list(map(lambda item: item**2, my_list)))
#
#
# # list sorting
#
# a = [(0,2), (4,3), (10,-1), (9,9)]
#
# print(sorted(a, key=lambda x: x[1]))

## comprehesion

# my_list = [num**2 for num in range(0, 100) if num % 2 == 0]
# print(my_list)
#
# ## in dict
#
# my_dict = {num:num*2for num in [1,2,3,4,5]}
# print(my_dict)

###
# some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
# duplicates = []
# for value in some_list:
#     if some_list.count(value) > 1:
#         if value not in duplicates:
#             duplicates.append(value)
# print(duplicates)
#
# duplicates2 = list(set(value for value in some_list if some_list.count(value) > 1 ))
# print(duplicates2)



# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True #changing this will either run or not run the message_friends function.
}


def authenticated(fn):
    def wrapper(*args, **kwargs):
        if args[0]['valid']:
            return fn(*args, **kwargs)
    return wrapper

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)