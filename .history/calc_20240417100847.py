calculation = True
previous_num = None
while calculation:
    if previous_num is None:
        num_1 = int(input("what is your first number?:\n"))
    else:
        num_1 = previous_num
        print(f"your selected number is {previous_num}")
    print("+\n-\n/\n*\n")
    # print("-")
    # print("*")
    # print("/")
    operator= input("Pick an operation:\n")
    num_2 = int(input("what is your next number?:\n"))
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
    if again == "y":
        calculation = True
        previous_num = add
    else:
        calculation = False
        