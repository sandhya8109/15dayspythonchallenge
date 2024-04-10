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

lives = 6

print(f"Psssst, the solution is {chosen_word}.")

display = []
for _ in range(word_length):
   display +="_"

while not end_of_game:
   guess  = input("Guess a letter:").lower()
   for position in range(word_length):
     letter =chosen_word[position]
     #print(f"Current position : {position} \n current letter:{letter}\n Guessed letter : {guess}")
     if letter == guess:
      display[position] = letter
if guess not in chosen_word: 
   lives-= 1
   if lives == 0:
    end_of_game = True
    print("you lose")     

   print(f"{''.join(display)}")  
   if "_" not in display:
     end_of_game = True
     print("You win")
   print(stages[lives])  