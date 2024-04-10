import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
end_of_game = False
word_list = ["sandhya", "rimal", "family"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
print(f"Psssst, the solution is {chosen_word}.")
display = []
word_length = len(chosen_word)
for _ in range(word_length):
   display +="_"

while not end_of_game:
   guess  = input("Guess a letter:").lower()
   for position in range(word_length):
     letter =chosen_word[position]
     #print(f"Current position : {position} \n current letter:{letter}\n Guessed letter : {guess}")
     if letter == guess:
      display[position] = letter
   print(f"{''.join(display)}")  
   if "_" not in display:
     end_of_game = True
     print("You win")