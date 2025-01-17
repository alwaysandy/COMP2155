import random

def guessingGame():
    numAttempts = 0
    targetNumber = random.randint(1, 100)
    while True:
        userGuess = input("Please guess a number between 1 and 100: ")
        if not userGuess.isdigit():
            print("Not a valid integer. Please try again..")
            continue
        if int(userGuess) < 1 or int(userGuess) > 100:
            print("Invalid input! Please enter a number between 1 and 100.")
            continue

        if int(userGuess) > targetNumber:
            if abs(int(userGuess) - targetNumber) <= 5:
                print("You're very close!")
            print("Too high! Try again..")
            numAttempts += 1
        elif int(userGuess) < targetNumber:
            if abs(int(userGuess) - targetNumber) <= 5:
                print("You're very close!")
            print("Too low! Try again..")
            numAttempts += 1
        else:
            numAttempts += 1
            print("Congrats! You guessed the correct number!")
            print(f"It took {numAttempts} attempts to guess the correct number!")
            break

# Ask the user if they want to play
while True:
    wantsToPlay = input("Would you like to play my guessing game? (Yes / No) ")
    if wantsToPlay.lower() == "yes":
        guessingGame()
        break
    elif wantsToPlay.lower() == "no":
        print("Maybe next time!")
    else:
        print("Please enter yes or no")
