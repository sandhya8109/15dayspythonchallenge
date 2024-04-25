import random
from artg import logo, vs
from data import data
def get_random_account():
    return random.choice(data)
name= ["Ashish", "Sandhya"]
position= ["It Guy", " Influencer"]
country = ["India", "Nepal"]
follower = [300, 1200]
print(f"Compare A :  {name[0]}, a {position[0]}, from {country[0]}.")
print("VS")
print(f"Against B :  {name[1]}, a {position[1]}, from {country[1]}.")
print("Who has more followers? Type 'A' or 'B'")
guess = input()
if guess == "A":
    guess == follower[0]
    if follower[0] > follower[1]:
        print(f"Yeah you are right.")
    else:
     print(f"sorry, that' not right.")    
else:
   guess = follower[1]  
   if follower[1] > follower[0]:
        print(f"Yeah you are right.")
        score = 1
        print("final score", score)    
   else:
     print(f"sorry, that' not right.") 
     score = 0     
     print("final score", score)   
