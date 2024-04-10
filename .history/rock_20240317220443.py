import random
human = input('what do you chose? type 0 for rock, 1 for paper or 2 for scissor.\n')
computer = random.randint(0,2)
print(f"computer choose {computer}")
if human == '0' and computer == '2':
    print('user wins')
elif human < computer:
    print('computer wins')   
else:
    print ("it's a draw")    

