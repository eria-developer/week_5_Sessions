# Dictionary
# Stores key-value kind of data 

# charactericstics of dictionaries 
# it is defined using curly braces
# it stores key-value pairs of data
# it is ordered
# It doesnt allow duplicate keys
# the keys are only meant to be immutable 

students_ages = {
    'Haruna': 14,
    'Libero': 17,
    2: 18,
    "Haruna": 37,
    "Sharifah": 20
}

# print(students_ages)

# # methods used in a dictionary
# # Adding key-value pairs to a dictionary 
# students_ages["Jibril"] = 16
# print(students_ages)

# students_ages["Sharifah"] = 80
# print(students_ages)

# students_fav_cities = dict()    # This is another way of initializing a dictionary
# print(students_fav_cities)

# students_fav_cities["Arua"] = "JAck"
# print(students_fav_cities)

# students_ages = dict()
# my_ages = list()
# my_foods = tuple()

# print(type(students_ages))
# print(type(my_ages))
# print(type(my_foods))

# students_ages = dict()
# students_ages = {}
# students_ages = dict(Kakumba=28, Jibril=34)
# print(students_ages)


# students_ages = {
#     'Haruna': 14,
#     'Libero': 17,
#     "Sharifah": 20
# }

# #Uing the update method
# students_ages.update({"Jack":98})
# print(students_ages)

# students_ages.update(Sharif=10)
# print(students_ages)


# # Deleting elements in a dictionary 
# # del 
# del students_ages['Haruna']
# print(students_ages)

# pop()
# my_list = [1, 4, 7]
# print(my_list)
# my_list.pop()
# print(my_list)

# students_ages = {
#     'Haruna': 14,
#     'Libero': 17,
#     "Sharifah": 20
# }
# # students_ages.pop("Libero")
# # print(students_ages)

# # dict.popitem()
# removed_element = students_ages.popitem()
# print(students_ages)
# print(removed_element)


# Accessing values in a dictionary
# students_ages = {
#     'Haruna': 14,
#     'Libero': 17,
#     "Sharifah": 20
# }

# students_ages['Sharifah']   # if the key doesnt exist, python throws an error
# # print(f"Sharifah's age is {students_ages['Sharifh']}")

# print(students_ages.get("Libro", 8977885))
# print(f"Libero's age is {students_ages.get("Libero")}")

# print(students_ages.get("Hruna", "Doesnt exist")  ) # incase haruna doesnt exist in the dictionary, python will return 0
# print(f"Haruna's age is {students_ages.get("aruna", "Doesnt exist")}")

students_ages = {
    'Haruna': 14,
    'Libero': 17,
    "Sharifah": 20
}

# dict.keys()     it displays the keys in the dictionary
# dict.values()   it displays all the values in the dictionary
# dict.items()    it displays all the key-values in the dictionary    

# print(students_ages.keys())
# print(students_ages.values())
# print(students_ages.items())


# for key, value in students_ages.items():
#     print(f"{key} is {value} years old")


# Ask the user fr their name,
# if their name is already in the dictionary, tell them they have already submitted their age
# otherwise, we tell them to enter their age
# we add their age and name to the urrent dictionary

students_ages = {
    'Haruna': 14,
    'Libero': 17,
    "Sharifah": 20
}

# while True:
#     name = input("What is your name: ")
#     if name in students_ages.keys():
#         print(f"Hey {name}, you have already submitted your age")
#         break
#     else:
#         age = input(f"Hey {name}, How old are you: ")
#         print(f"Thank you for participating {name}, your age {age} has been added to the database")
#         print(f"{name}: {age}")
#         students_ages[name] = age
#         break


# for key, value in students_ages.items():
#     print(f"{key}: {value}")
# dict.clear()
# print(f"Students age current database: {students_ages}")
# students_ages.clear()
# print(f"Students age current database: {students_ages}")


# dict.copy()
# copied_student_ages = {}
# print(copied_student_ages)
# copied_student_ages = students_ages.copy()
# print(copied_student_ages)


# Nested Dictionaries 

# my_students_profiles = {
#     "libero" : {
#         "fullname": "Haruna Libero",
#         "age": 15,
#         "favorite_language": "Python"
#     },
#     "priscillah": {
#         "fullname": "Prisicillah Kyamulabi",
#         "age": 14,
#         "favorite_language": "Javascript"
#     }
# }

# # print(my_students_profiles["priscillah"]["fullname"])
# # print(f"Lberos fullname is {my_students_profiles['libero']['fullname']}")


# for key, value in my_students_profiles.items():
#     print(f"\n{key}")
#     for inner_key, inner_value in value.items():
#         print(f"---{inner_key}: {inner_value}---")



# SETS 
# it is used to store unique unordered elements 
# it is defined using the set() or using {} but not empty {}
# it doesnot accespt duplicates
# it is unordered

my_set = set()
print(my_set)

my_set = {"Putple", "Sleeeping", "Blue", "Blue", "Blue"}
print(my_set)

# set operations 
# set_1 = {1, 2, 3, 4, 5}
# set_2 = {1, 3, 5, 7, 9}
# set_3 = {1, 5, 7}
# set_4 = {1, 2, 3, 4, 5, 6, 7, 8, 9}

# print(set_1 | set_2)
# print(set_1 & set_2)
# print(set_1 - set_2)
# print(set_2 - set_1)
# print(set_1 ^ set_2)
# print(set_3 <= set_4)
# print(set_4 >= set_3)

# print(set_3.issubset(set_4))
# print(set_4.issuperset(set_3))
# print(set_1.isdisjoint(set_2))



# Set Methods 
# adding elements to a a set 
# set.add()
my_set = {2, 8, "Food"}
print(my_set)

my_set.add("Purple")
print(my_set)

# removing elements froma  set 
# set.remove()
# my_set.remove(1)    # will throw an error

# set.discard()
my_set.discard("Food")
print(my_set)

my_set.discard("foods")
print(my_set)

# pop()
my_set = {2, 8, "Food", "Blue", "Apples"}
my_set.pop()
print(my_set)