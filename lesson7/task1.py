# Task 1
#
# Make a program that has some sentence (a string)
# on input and returns a dict containing all unique words
# as keys and the number of occurrences as values.

a = input("Enter the string: ")
my_dict = {i: a.count(i) for i in a}
print(my_dict)
