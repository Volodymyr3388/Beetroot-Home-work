import random
i = 1
while i == 1:
    player = int(input("Please enter the number: "))
    computer = random.randint(1, 10)
    result = (player, computer)
    if player == computer:
        print(result,"You Win")
    else:
        print(result,"You lose")

