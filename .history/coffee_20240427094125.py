from menu import MENU
def get_order():
    user= input("What would you like?(espresso/latte/cappuccimo):\n")
    if user == "espresso":
       return MENU["espresso"]
get_order()