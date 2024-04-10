alphabet = ['a', 'b','c','d', 'e','f','k', 'l','m','n', 'o','p','g','h','i','j','q','r', 's','t','u','v','w','x','y', 'z']
def encrypt(msgs, shifts):
   text = ""
   for letter in msgs:
    position = alphabet.index(letter)
    new_position = position + shifts
    if new_position >= len(alphabet):
     new_position = new_position % len(alphabet) - 1
    new_letter = alphabet[new_position]    
    text += new_letter 
   print(f"The encode text is {text}")
   return text
def decrypt(msgs, shifts):
   text = ""
   for letter in msgs:
      position = alphabet.index(letter)
      new_position = position - shifts
      if new_position < 0:
       new_position = len(alphabet) - abs(new_position) % len(alphabet) + 1
      print(new_position)
      new_letter = alphabet[new_position]
      text += new_letter
   print(f"The decode text is {text}")
while (True):   
   direction =input("Type'encode' to encrypt ,  type'decode' to decrypt:\n")
   msg = input('Type your message:\n')
   num = int(input('Type the shift:\n'))
   if direction == "encode":
      encrypt(msgs = msg , shifts = num) 
   else:  
      decrypt(msgs= msg, shifts = num)  
   again = input("type 'yes' if you want to go again, otherwise type 'no':\n") 
   if again == "no":
     break
    