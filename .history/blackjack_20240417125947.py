import random
def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10 ,10]
    card =  random.choice(cards)
    return card
user_card = []
computer_card = []
for _ in range(2):
    user_card.append(deal_cards)
    computer_card.append(deal_cards)

computer = input("computer's first card:\m")
again = input("type 'y' to get another card , type'n' to pass:\n")
final = computer_final = computer
if final > computer_final:
    print("you win")
else:
    print("computer wins")  
if card => 21:
    print("you lose")       
