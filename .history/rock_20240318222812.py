import random
human = int(input('what do you chose? type 0 for rock, 1 for paper or 2 for scissor.\n'))
computer = random.randint(0,2)
print(f"computer choose {computer}")
if computer == 2 and human == 0:
    print('you win')
elif human == 2 and computer == 0:
    print('you lose')
elif computer < human:
    print('you win ')
elif computer == human:
    print("it's a draw")
else:  # This block handles the case where computer > human
    print("you lose") 
 