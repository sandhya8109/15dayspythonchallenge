import random
letter = ['a', 'b','c','d', 'e','f','k', 'l','m','n', 'o','p','g','h','i','j','q','r', 's','t','u','v','w','x','y', 'z', 'A', 'B','C','D', 'E','F','K', 'L','M','N', 'O','P','G','H','I','J','Q','R', 'S','T','U','V','W','X','Y', 'Z']
number = ['0','1','2', '3','4','5', '6','7','8', '9']
symbol = ['!', '@','#','$', '%','&','*', '_','(',')', '+']
print('Welcome to the PyPassword Generator!')
letters = int(input('How many letters would you like in  your password?'))
symbols = int(input('How many symbols would you like?'))
numbers = int(input('How many numbers would you like?'))
password = ''
for char in range(1, letters + 1):
  password += random.choice(letter)
for char in range(1, numbers + 1):
  password += random.choice(number)  
for char in range(1, symbols + 1):
  password += random.choice(symbol)
print(f"Here is your password: {password}.")