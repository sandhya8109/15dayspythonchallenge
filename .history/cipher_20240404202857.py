alphabet = ['a', 'b','c','d', 'e','f','k', 'l','m','n', 'o','p','g','h','i','j','q','r', 's','t','u','v','w','x','y', 'z', 'a', 'b','c','d', 'e','f','k', 'l','m','n', 'o','p','g','h','i','j','q','r', 's','t','u','v','w','x','y', 'z']

direction =input("Type'encode' to encrypt ,  type'decode' to decrypt")
msg = input('Type your message:')
num = input('Type the shift:')
cipher_text = ""
def encrypt(msgs, shifts):
   for letter in msgs:
    position = alphabet.index(letter)
    new_position = position + shifts
    new_letter = alphabet[new_position]    
    cipher_text += new_letter 
print(f"Here's the encode text {cipher_text}")
encrypt(msgs = msg , shifts = num)
again = input("type 'yes' if you want to go again, otherwise type 'no':") 