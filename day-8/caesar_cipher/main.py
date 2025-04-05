alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


#TODO-1: Create a function call encrypt() that takes orginal_text and shift_amount as 2 input

def encrypt(original_text, shift_amount):
    original_text_list = list(original_text)
    encrypt_text_list = []
    for char in original_text_list:
        encrypt_text_list.append(chr(ord('a') + (ord(char) + shift_amount- ord('a'))%26))
    encrypt_text = "".join(encrypt_text_list)
    return encrypt_text

encrypt_text = encrypt(text, shift)
print(encrypt_text)


#TODO-2: Inside encrypt -> shift original text by shift amount

#TODO-3: Call 'encrypt()' function and pass the user inputs.