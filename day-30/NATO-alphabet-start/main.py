#---- my code -------------------------------------------------------------

import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
# ------------------- my solution ------------------------------------------
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}

# def NATO_alphabet_game():
#     word = input("Enter a word:").upper()
#     output_list = [phonetic_dict[letter] for letter in word]
#     return output_list

# try:
#     output_list = NATO_alphabet_game()
# except KeyError:
#     still_error = True
#     while still_error:
#         print("Sorry only letters in the alphabet please.")
#         try:
#             output_list = NATO_alphabet_game()
#         except KeyError:
#             still_error = True
#         else:
#             still_error = False
# finally:
#     print(output_list)

# ------------- teacher solution ---------------------
    
def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()
