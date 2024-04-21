import random
from ar import logo 
print (logo)
def number():
    random_number = random.randint(1, 100)
    #print("The guess for a number between 1 and 100. is :", random_number)
    return random_number
accept = number()
print(accept)
number_of_guess = 0
rule = input("Do you want to play it hard or easy? type 'hard' for hard level and 'easy' for easy level:\n")
if rule == "hard":
    print("you can make 5 guess")
    number_of_guess = 5
else:
    number_of_guess = 10

    
def if_win():
    if user_pick > accept:
        print("your guess is too high")
    elif user_pick == accept: 
        print("you win as your guess is correct")   
    else:
        print("your guess is too low")   
is_won = False             
for _ in range(number_of_guess):
    user_pick =  int(input("Please pick your number\n: "))
    is_win = if_win(user_pick, accept)
    if(is_win == True):
        is_won=True
        break
if(is_won==False):
    print("You lost")
  

