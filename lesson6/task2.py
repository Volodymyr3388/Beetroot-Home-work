# Task 2
#
# Exclusive common numbers.
#
# Generate 2 lists with the length of 10 with random integers from 1 to 10, and make a third list containing the common integers between the 2 initial lists without any duplicates.
#
# Constraints: use only while loop and random module to generate numbers
from random import randint
a = []
b = []
c = []
i = 0
while i in range(10):
    a.append(randint(0, 10))
    b.append(randint(0, 10))
    i += 1

c = list(set(a) & set(b))
print(a)
print(b)
print(c)
