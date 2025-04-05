alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


#TODO-1: Create a function call encrypt() that takes orginal_text and shift_amount as 2 input

def encrypt(original_text, shift_amount):
    original_text_list = list(original_text)
    encrypt_text_list = []
    for char in original_text_list:
        if ord(char) >= ord("a") and ord(char) <= ord("z"): 
            encrypt_text_list.append(chr(ord('a') + (ord(char) + shift_amount- ord('a'))%26))
        else:
            encrypt_text_list.append(char)
    encrypt_text = "".join(encrypt_text_list)
    return encrypt_text

def decrypt(encrypted_text, shift_amount):
    encrypt_text_list = list(encrypted_text)
    decrypt_text_list = []
    for char in encrypt_text_list:
        if ord(char) >= ord("a") and ord(char) <= ord("z"): 
            decrypt_text_list.append(chr(ord('a') + (ord(char) - shift_amount- ord('a'))%26))
        else:
            decrypt_text_list.append(char)
    decrypt_text = "".join(decrypt_text_list)
    return decrypt_text

if direction == "encode":
    encrypt_text = encrypt(text, shift)
    print(encrypt_text)
elif direction == "decode":
    decrypt_text = decrypt(text, shift)
    print(decrypt_text)


#TODO-2: Inside encrypt -> shift original text by shift amount

#TODO-3: Call 'encrypt()' function and pass the user inputs.