word_list = ["Sandhya", "Rimal", "Family"]
import random
chosen_word = random.choice(word_list)
display = []
for _ in chosen_word:
  display +="_"
print(display)  
guess  = input("Guess a letter:").lower()
for letter in chosen_word:
  if letter == guess:
   print(letter)
  else:
    print("_")  
