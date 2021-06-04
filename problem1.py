#Number guessing game

def number_guess():    
    import random
    number = random.randint(0,100)
    guess_check = None

    print("welcome to Number Guess game")

    while guess_check != number:
        guess_check = int(input("Enter the Number b/w 0 to 100: "))

        if guess_check > number:
            print("you enter number is Too high")
        elif guess_check < number:
            print('you enter number is Too Low')
        else:
            print("you enter number is just right")

    print("Thank you")

print(number_guess())
