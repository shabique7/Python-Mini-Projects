from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def ceaser(original_text,shift_amount,todo):
    cipher_text = ""
    for letter in original_text:
        if letter not in alphabet:
            cipher_text += letter
        else:
            if todo == "encode":
                shift = alphabet.index(letter) + shift_amount
                if shift <= 25:
                    cipher_text += alphabet[shift]
                else:
                    shift = shift-26
                    cipher_text += alphabet[shift]
            elif todo =="decode":
                shift = alphabet.index(letter) - shift_amount
                if shift >= 0:
                    cipher_text += alphabet[shift]
                else:
                    shift = shift + 25
                    cipher_text += alphabet[shift]
    print(f'Here is the {todo}d result:\n{cipher_text}')
ceaser(text,shift,direction)






