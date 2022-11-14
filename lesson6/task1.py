# Task1
# The greatest number
#
# Write a Python program to get the largest number from a list of random numbers with the length of 10
#
# Constraints: use only while loop and random module to generate numbers
from random import randint
a = []
i = 0
while i in range(10):
    a.append(randint(0, 100))
    i += 1
print(a)
print(max(a))
