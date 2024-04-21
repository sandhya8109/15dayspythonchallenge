import random
from ar import logo 
print (logo)
def number():
    random_number = random.randint(1, 100)
    #print("The guess for a number between 1 and 100. is :", random_number)
    return random_number
pick = int("pick a guess:\n")
    if pick > accept:
        print("your guess is too high")
    elif pick == accept: 
        print("you win as your guess is correct")   
    else:
        print("your guess is too low")        


accept = number()
print(accept)
rule = input("Do you want to play it hard or easy? type 'hard' for hard level and 'easy' for easy level:\n")
if rule == "hard":
    print("you can make 5 guess")
    
def guess():
    