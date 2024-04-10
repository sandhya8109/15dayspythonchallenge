import random
computer = random.randint(0,2)
print(computer)
human = input('what do you chose? type 0 for rock, 1 for paper or 2 for scissor')
if human == '0' and computer == '1':
    print('computer wins')
elif human == '1' and computer == '2':
    print('computer wins')   
elif human == computer:
    print ("it's a draw")    
else:
    print('human wins')
