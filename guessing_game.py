guess = 0

while guess != 7:
    guess = int(input("Guess a number: "))

    if guess == 7:
        print("You Win!")
    elif guess > 7:
        print("Too High")
    else:
        print("Too Low")