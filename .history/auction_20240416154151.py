from art import logo
print (logo)
bid = {}
def clear():
  print("\033c")  # This code uses ANSI escape sequence to clear the console

# Calling the clear() function
clear()
bidding_finished = False
def find_highest_bidder(bidding_record):
   highest_bid = 0
   winner = ""
   for bidder in bidding_record:
      bid_amount = bidding_record[bidder]
      if bid_amount > highest_bid:
         highest_nid = bidding_record
         winner = bidder
   print(f"The winner is {winner} with a bid of ${highest_bid}")     
while not bidding_finished:   
   print("Welcome to the secret auction program")
   name = input("What is your name?:\n")
   price = input("What is your bid?:\n")
   bid[name] = price
   again = input("Are there any other bidder? type 'yes' or 'no' :\n")  
   if again == "no":
      bidding_finished = True
      find_highest_bidder(bids)
   elif again =="yes":
      