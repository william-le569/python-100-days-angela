# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}

# #TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.

#---- my code ---

import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
# --------------------------------------------------------------------------
# My solution
# dict_data = {}
# for (index, row) in data.iterrows():
#     dict_data[row.letter] = row.code

# name = input("Enter your name?:")

# name_list = [value for letter in name for (key, value) in dict_data.items() if letter.lower() == key.lower()]

# print(name_list)
# ---------------------------------------------------------------------------

# teacher solution
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

word = input("Enter a word:").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)