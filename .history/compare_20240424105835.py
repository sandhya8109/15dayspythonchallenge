name= ["Ashish", "Sandhya"]
position= ["It Guy", " Influencer"]
country = ["India", "Nepal"]
follower = [300, 1200]
print(f"Compare A :  {name[0]}, a {position[0]}, from {country[0]}.")
print("VS")
print(f"Against B :  {name[1]}, a {position[1]}, from {country[1]}.")
print("Who has more followers? Type 'A' or 'B'")
guess = int(input())
if guess == "A":
    guess == follower[0]
    if guess > follower[1]:
        print(f"Yeah you are right.")
    else:
     print(f"sorry, that' not right.")    
else:
   guess = follower[1]  
   if guess > follower[0]:
        print(f"Yeah you are right.")
   else:
     print(f"sorry, that' not right.")      