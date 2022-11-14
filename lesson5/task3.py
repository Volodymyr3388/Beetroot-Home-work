import random
word = list(input("Enter the word: "))
for i in range(5):
    a = ""
    for i in word:
        a += random.choice(word)
    print(a)

# import random
# word = input("Enter the word: ")
# for i in range(5):
#     print(" ".join(random.choice(word)for j in range(len(word))))

