
print("Question 1")

# declare the list
#           0,      1,  2,         3, 4,    5
my_list = ["Apple", 101, "Orange", 102, "Cat", 103]
my_list.append("Ball")
# Tell the user what your list contains
print("This list contains numbers and strings.")
# Tell the user to put and take input from the user and assign to variable
index = int(input("Enter the index you want to display: "))

# Tell the users the index they put and it's appropriate
print(f"You Entered index {index} which is appropriate to: {my_list[index]} ")



print("Question 2")
# declare dictionary
marks = {
    str(input("Enter course name: ")): int(input("Enter course marks: ")),
    str(input("Enter course name: ")): int(input("Enter course marks: ")),
    str(input("Enter course name: ")): int(input("Enter course marks: ")),
    str(input("Enter course name: ")): int(input("Enter course marks: "))
}
# print out what user entered
print(f"Your dictionary is: {marks}")
print(f"Your keys are: {marks.keys()}")
print(f"Your Values are: {marks.values()}")
