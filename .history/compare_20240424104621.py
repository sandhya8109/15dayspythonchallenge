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
    print(f"sorry, that's wrong.")
else:
    print(f"Yeah, that's right.")    