print('welcome to the tip calculator.')
total = float(input('what was the total bill?\n'))
people = int(input('How many people to split the bill?\n'))
discount = int(input('what percentage tip would you lie to give?10 , 12 , or 15?\n'))
split = total / people 
tip = total * discount / 100
add = tip + total 
result = add / people        
print ("Each person should pay :" , result)



