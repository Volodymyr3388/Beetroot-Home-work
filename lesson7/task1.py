# Task 1
#
# Make a program that has some sentence (a string)
# on input and returns a dict containing all unique words
# as keys and the number of occurrences as values.

a = input("enter the string: ")
b = {}
c = a.split()
for i in c:
    if i not in b:
        b[i] = c.count(i)
    else:
        pass

print(b)
