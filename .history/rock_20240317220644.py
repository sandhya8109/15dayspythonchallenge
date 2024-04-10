import random
human = int(input('what do you chose? type 0 for rock, 1 for paper or 2 for scissor.\n'))
computer = random.randint(0,2)
print(f"computer choose {computer}")
if human == '0' and computer == '2':
    print('user wins')
elif human < computer:
    print('computer wins')   
elif computer == human:
    print('it a draw')    
else:
    print ("you typed an invalid number, you lose")    

