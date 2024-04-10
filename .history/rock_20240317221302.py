import random
human = int(input('what do you chose? type 0 for rock, 1 for paper or 2 for scissor.\n'))
computer = random.randint(0,2)
print(f"computer choose {computer}")
if computer >= 3 or human <=0:
    print ("you typed an invalid number, you lose")    
elif human == '2' and computer == '0':
    print('computer wins')
elif  human == '1' and computer == '2':
    print('computer wins')   
elif computer == human:
    print('it a draw')   
elif computer == '1' and human == '0':
          print('computer wins')    
else:
     print('human win')           


