# I'm planning my wedding and trying to keep track of who's RSVPed 
# and their meal choice (chicken, fish, or vegetarian). 
# How can I store this information so I can easily look up what each guest is eating?

meals_for_my_wedding_guests = {
    "Allan": "Salads",
    "Jack": ["Chicken", "A drink", "Fish"],
    "HAruna": "Fish",
    "Prisillah": None
}

# Student Grade Calculator
# ----------------------------------
# You are a teacher with the following student test scores:
# student_grades = {
#     "Alice": [85, 92, 78],
#     "Bob": [88, 86, 92],
#     "Charlie": [75, 82, 79]
# }

# Tasks:
# a) Calculate and return the average grade for each student
# b) Add a new test score of 90 for Alice
# c) Find and return the name of the student with the highest average


# You want to store ages for your friends
# You are going to first have a database containing some values
# my_friends_ages = {
#     "Allan": 45,
#     "Alex": 21,
#     "Linda": 57
# }
# Then you will ask your friends for their names and if their name is already in the database, tell them you already have themm in the db
# Then you move to the next friend
#If their name is not in the db, then go on and ask for their age
# Then store their age in the db
# After that, you get the sum of all your friends' ages


my_database = {
    "Allan": 45,
    "Alex": 21,
    "Linda": 57
}

print(f"Enter 'quit' as your name, to quit the program")
while True:
    name = input("\nEnter your name: ")
    if name == "quit":
        break

    if name in my_database.keys():
        print(f"Hello {name}, you are already in the database\nThank you for participating")
        continue
    else:
        age = int(input(f"Hey {name}, could you please enter your age: "))
        my_database[name] = age

print()
for name, age in my_database.items():
    print(f"{name} is {age} years old")

# print("\n\n")
# sum_of_ages = 0
# for age in my_database.values():
#     sum_of_ages = sum_of_ages + age
# print(f"The sum of my friends' ages is {sum_of_ages}")

print()
sum_of_ages = 0
for name, age in my_database.items():
    sum_of_ages = sum_of_ages + age
print(f"The sum of my friends' ages is {sum_of_ages}")



# Student Grade Calculator
# ----------------------------------
# You are a teacher with the following student test scores:
# student_grades = {
#     "Alice": [85, 92, 78],
#     "Bob": [88, 86, 92],
#     "Charlie": [75, 82, 79]
# }

# Tasks:
# a) Calculate and return the average grade for each student
# b) Add a new test score of 90 for Alice
# c) Find and return the name of the student with the highest average
