num_1 = input("what is your first number?:\n")
print("+\n -\n/\n*\n")
# print("-")
# print("*")
# print("/")
operator= input("Pick an operation:\n")
num_2 = input("what is your next number?:\n")
if operator == '+':
    add= num_1 + num_2
    print(f"{num_1} {operator} {num_2} = {add}")
elif operator == '/':
    add= num_1 / num_2
    print(f"{num_1} {operator} {num_2} = {add}")
elif operator == '*':
    add= num_1 * num_2
    print(f"{num_1} {operator} {num_2} = {add}")
elif operator == '-':
    add= num_1 - num_2
    print(f"{num_1} {operator} {num_2} = {add}")
again = input(f"Type 'y' to continue calculating with {add} , or type 'n' to start a new calculation:\n")
if again == "n":
   calculation = True
elif again =="y":
     