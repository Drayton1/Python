import random

guess = int(input('Your guess is: '))
correctNumber = random.randint(1,20)
guessCount = 1

while guess != correctNumber:
    guessCount += 1
    
    if guess < correctNumber:
        guess = int(input('Guess higher. Your guess is: '))
    else:
        guess = int(input('Guess lower. Your guess is: '))
        
print(f"You got it! It took you {guessCount} guesses.")
