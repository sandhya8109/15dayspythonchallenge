print('Welcome to Treasure Island')
print('Your mission is to find the treasure')
path= input("You're at a cross road. Where do you want to go? Type 'left' or 'right'\n")
if (path == 'right'):
    print('Sorry , you fall into a hole. Game Over!!')
else:
   print('You come to a lake.')
   path_2 = input('There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across:\n')
   if (path_2 == 'swim'):
    print('Sorry you are attacked by trout. Game Over!!')
   else:
   print('Move toward the door.')
   path_3 = input('There is a door  in the after passing the lake. Type "blue" to go toward red door. Type "blue" to go toward blue door:\n')   
     if (path_3 == 'red'):
       print('Sorry you are burned by fire. Game Over!!')
     elif(path_3 == 'blue'):
       print('Sorry you are eaten by beast. Game Over!!')
     else:
       print('Congratulation you win')
    