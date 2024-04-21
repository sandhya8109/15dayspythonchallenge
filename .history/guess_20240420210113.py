import random
from ar import logo 
print (logo)
def number():
    random_number = random.randint(1, 100)
    #print("The guess for a number between 1 and 100. is :", random_number)
    return random_number
accept = number()
print(accept)
rule = input("Do you want to play it hard or easy? type 'hard' for hard level and 'easy' for easy level:\n")
if rule == "hard":
    print("you can make 5 guess")
    
