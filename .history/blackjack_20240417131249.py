import random
def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10 ,10]
    card =  random.choice(cards)
    return card
user_card = []
computer_card = []
is_game_over = False
for _ in range(2):
    user_card.append(deal_cards())
    computer_card.append(deal_cards())
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) >21 :
        cards.remove(11)
        cards.append(1)
user_score = calculate_score(user_card)   
computer_score = calculate_score(computer_card)  
print(f"your card : {user_card}")
print(f"computer card : {computer_card}")
if user_score == 0 or computer_score == 0 or user_score > 21:       
    is_game_over = True


# computer = input("computer's first card:\m")
# again = input("type 'y' to get another card , type'n' to pass:\n")
# final = computer_final = computer
# if final > computer_final:
#     print("you win")
# else:
#     print("computer wins")  
# if card => 21:
#     print("you lose")       
