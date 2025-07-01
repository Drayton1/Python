#Objective: Print a random fortune for the user.
import random
'''look into modules on W3 for the functions for random module'''

luckyNum = random.randint(1,1000)
fortuneNum = random.randint(1,3)
fortuneText = ''
if fortuneNum == 1:
    print(f"You'll get that promotion! You\'re lucky number is: {luckyNum}")
if fortuneNum == 2:
    print(f"You'll get that deal! You\'re lucky number is: {luckyNum}")
if fortuneNum == 3:
    fortuneText = "You will complete that project."
    print(f"{fortuneText} You\'re lucky number is: {luckyNum}")
