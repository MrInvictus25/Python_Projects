while True:
  from art import logo
  print(logo)
  
  alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26

  def caesar(text = text, shift = shift, direction = direction):
    cipher = ''
    if direction == 'decode':
      shift *= -1
    for character in text:
      if character in alphabet:
        result = alphabet.index(character)
        cipher += alphabet[result + shift]
      else:
        cipher += character
    print(f"Here's the {direction}d result: {cipher}")
    
  caesar(text = text, shift = shift, direction = direction)
  new_message = input("Would you like to encrypt or decrypt one more time: Yes/No? ")
  if new_message.lower() == "no":
    break
