# DICTIONARY
# It stores key-value pairs
# it is defined using {}
# doesnt allow duplicate keys
# we can define a dictonary using a dict()

# my_students_ages = {}
# print(type(my_students_ages))

# my_students_ages = {
#     "Eliot": 12,
#     "Linda": 17,
#     "Vanessa": 29,
#     "Joshua": 15
# }
# print(my_students_ages)

# my_other_dictionary = dict()
# print(my_other_dictionary)


# # Accessing elements ina  dictionary 
# # dict[key] => if the key used doesnt exist, python throws a keyerror
# print(my_students_ages["Vanessa"])
# # print(my_students_ages["Lind"])     # throws  a key error

# # dict.get(key)
# print(my_students_ages.get("Eliot"))
# print(my_students_ages.get("Elot"))
# print(my_students_ages.get("Elot", "Key doesnt exist"))


# Adding and updating elements ina  dictionary 
# my_students_ages = {
#     "Eliot": 12,
#     "Linda": 17,
#     "Vanessa": 29,
#     "Joshua": 15
# }
# # dict[key] = value 
# # print(my_students_ages)
# # my_students_ages["Doug"] = 38   
# # print(my_students_ages)

# # my_students_ages["Eliot"] = 139
# # print(my_students_ages)

# # update()
# # print(my_students_ages)
# # my_students_ages.update({"Doug":89})
# # print(my_students_ages)
# # my_students_ages.update(Melissa=78)
# # print(my_students_ages)

# # my_students_ages.update({"Linda": 150})
# # print(my_students_ages)


# # Removing Elements from a dictionary 
# # del dict["key"]
# # del my_students_ages["Linda"]
# # print(my_students_ages)


# # # pop() method 
# # # my_students_ages.pop("Vanessa")
# # # print(my_students_ages)

# # # popitem()
# # my_students_ages.popitem()
# # print(my_students_ages)


# my_students_ages = {
#     "Eliot": 12,
#     "Linda": 17,
#     "Vanessa": 29,
#     "Joshua": 15
# }

# # dict.keys()
# print(my_students_ages.keys())

# # dict.values()
# print(my_students_ages.values())

# # dict.items()
# print(my_students_ages.items())


# # Looping in dictionaries 
# for key in my_students_ages.keys():
#     print(key)

# for value in my_students_ages.values():
#     print(value)

# for key, value in my_students_ages.items():
#     print(f"{key} is {value} years old")



# # Nested Dictionaries 
# my_students_instagram_profiles = {
#     "am_josh256": {
#         "fullname": "Mugabe Joshua",
#         "age": 16,
#         "favorite_language": "Pyhton"
#     },
#     "lind_anything": {
#         "fullname": "Letaru Linda",
#         "age": 18,
#         "favorite_language": "Javascript"
#     }
# }

# print(my_students_instagram_profiles["am_josh256"]["fullname"])
# print(my_students_instagram_profiles["lind_anything"]["age"])

# for key, value in my_students_instagram_profiles.items():
#     print(f"-------{key}-------")
#     for inner_key, inner_value in value.items():
#         print(f"{inner_key}: {inner_value}")



# # Ask the user fr their name,
# # if their name is already in the dictionary, tell them they have already submitted their age
# # otherwise, we tell them to enter their age
# # we add their age and name to the urrent dictionary

# students_ages = {
#     "Eliot": 12,
#     "Vanessa": 14,
#     "Matthew": 29,
#     "Linda": 10
# }


# # SETS 
# # It is unorderdred 
# # It doesnt allow duplicate elements 
# # They are dfined with a set() for an empty set and curry braces for not empty set 

# my_set = {"Food", "Sleeping", 45, 78, "Sleeping"}
# print(my_set)


# adding elements to a set
# add() method
# my_set = {"Food", 2}
# print(my_set)
# my_set.add("Sleeping")
# print(my_set)

# # Removing elements from a set 
# # remove() method 
# # my_set.remove(22)
# print(my_set)


# # discard()
# # my_set.discard("Fod")
# print(my_set)

# # pop()
# my_set.pop()
# print(my_set)

# Set operations
# set_1 = {1,2,3,4,5}
# set_2 = {1,3,5}

# print(set_1 | set_2)
# print(set_1 & set_2)
# print(set_1 - set_2)
# print(set_2 - set_1)
# print(set_1 ^ set_2)
# print(set_1 <= set_2)
# print(set_1 >= set_2)
# print(set_1.issubset(set_2))
# print(set_1.issuperset(set_2))




phrase = input("Enter a phrase")
nums = {
   "0":"zero",
   "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
    "7":"seven",
    "8":"eight",
    "9":"nine",
}
 
for i in phrase:
    if '10' in phrase:
    	phrase = phrase.replace('10', 'ten')
    elif i in nums.keys():
        phrase = phrase.replace(i, nums[i])
print(phrase )