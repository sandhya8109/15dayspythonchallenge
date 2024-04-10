alphabet = ['a', 'b','c','d', 'e','f','k', 'l','m','n', 'o','p','g','h','i','j','q','r', 's','t','u','v','w','x','y', 'z', 'a', 'b','c','d', 'e','f','k', 'l','m','n', 'o','p','g','h','i','j','q','r', 's','t','u','v','w','x','y', 'z']

direction =input("Type'encode' to encrypt ,  type'decode' to decrypt:\n")
msg = input('Type your message:\n')
num = int(input('Type the shift:\n'))

def encrypt(msgs, shifts):
   text = ""
   for letter in msgs:
    position = alphabet.index(letter)
    new_position = position + shifts
    new_letter = alphabet[new_position]    
    text += new_letter 
   print(f"The encode text is {text}")
#encrypt(msgs = msg , shifts = num)
again = input("type 'yes' if you want to go again, otherwise type 'no':") 