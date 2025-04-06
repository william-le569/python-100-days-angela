alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#TODO-1: Create a function call encrypt() that takes orginal_text and shift_amount as 2 input

import art

print(art.logo)

def caesar_cipher(original_text, shift_amount, direction):
    if direction == "decode":
        shift_amount *= -1
    original_text_list = list(original_text)
    output_text_list = []
    for char in original_text_list:
        if ord(char) >= ord("a") and ord(char) <= ord("z"): 
            output_text_list.append(chr(ord('a') + (ord(char) + shift_amount- ord('a'))%26))
        else:
            output_text_list.append(char)
    output_text = "".join(output_text_list)
    print(f"Here is the {direction} result: {output_text}.")

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar_cipher(original_text=text, shift_amount=shift, direction=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("Good bye!")

#TODO-2: Inside encrypt -> shift original text by shift amount

#TODO-3: Call 'encrypt()' function and pass the user inputs.