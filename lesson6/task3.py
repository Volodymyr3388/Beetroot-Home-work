# Extracting numbers.
#
# Make a list that contains all integers from 1 to 100, then find all integers from the list that are divisible by 7 but not a multiple of 5, and store them in a separate list. Finally, print the list.
#
# Constraint: use only while loop for iteration

a = []
i = 0
while i in range(0, 101):
    if i % 7 == 0 and i % 5 != 0:
        a.append(i)
    i += 1
print(a)

