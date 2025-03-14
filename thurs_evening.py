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

student_grades = {
    "Alice": [85, 92, 78],
    "Bob": [88, 86, 92],
    "Charlie": [75, 82, 79]
}

student_averages = {}   #empty dic to store the averages for each student
for key, value in student_grades.items():
    sum_of_scores = 0
    for num in value:
        sum_of_scores = sum_of_scores + num
    num_of_scores = len(value)      # 3
    average = round(sum_of_scores / num_of_scores, 2)
    student_averages[key] = average
print(student_averages)


student_grades["Alice"].append(90)

highest_average = 0
highest_student_average = ""

for key, value in student_averages.items():
    if value > highest_average:
        highest_average = value
        highest_student_average = key

print(highest_student_average, highest_average)



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



# Store Inventory Manager
# ---------------------------------
# You manage a small grocery store with this inventory:
# inventory = {
#     "apple": {"price": 0.50, "quantity": 100},
#     "banana": {"price": 0.75, "quantity": 150},
#     "orange": {"price": 0.60, "quantity": 75}
# }

# Tasks:
# a) Returns all products with quantity less than 80
# b) Calculate the total value of your inventory (price * quantity for each item)
# c) Update the price of bananas to $0.80

# Example output for part a):
# {"orange": 75}



# Contact Manager
# --------------------------
# Start with this phone directory:
# phone_directory = {
#     "John Smith": "555-0123",
#     "Mary Johnson": "555-4567",
#     "David Wilson": "555-8901"
# }

# Tasks:
# a) add a new contact, making sure you don't duplicate entries
# b) delete a contact
# c) update an existing contact's number
# d) find all contacts that start with a given letter

# Example output for part d) with letter "M":
# {"Mary Johnson": "555-4567"}
