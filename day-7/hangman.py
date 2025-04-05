import random

from hangman_words import word_list

# word_list = ["aardvard", "baboon", "camel"]

cursed_phrase_list = ["Guess wrong again... the hangman's sharpening his axe just for you.", 
                      "One more mistake and your stickman gets a stylish noose necklace!",
                      "You sure about that letter? I’d hate to see your stickman lose another limb...",
                      "You’re just one wrong guess away from a career in ghosting—literally.",
                      "If you get this wrong, I’ll start writing your farewell letter."
                      ]

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


# Randomly choose a word

keyword = random.choice(word_list)

# print(keyword)
# print(len(keyword))

keyword_list = []
for char in keyword:
    keyword_list.append(char)

blank = []

for i in range(0, len(keyword)):
    blank.append("_")

print(HANGMANPICS[0])
print("".join(blank))
# Ask player to guess a letter

nr_lives = 6
is_guessed = False
is_victory = False

def is_victory(my_list):
    for char in my_list:
        if char == "_":
            return False
    return True

correct_word_list = []

while nr_lives > 0:
    blank_str = ""
    print("#####################################################################")
    print(f"----------------YOU HAVE {nr_lives}/6 LIVES LEFT------------- ")
    guessed_letter = input("Please guess a letter: ").lower().strip()
    if guessed_letter in correct_word_list:
        print(f"You have entered {guessed_letter} letter you've guessed. Please enter other letter!")
        continue

    for i in range(0, len(keyword_list)):
        if guessed_letter == keyword_list[i]:
            blank[i] = guessed_letter
            if guessed_letter not in correct_word_list:
                correct_word_list.append(guessed_letter)
            is_guessed |= True
    blank_str = blank_str.join(blank)
    if not is_guessed:
        nr_lives -= 1
        if nr_lives == 5:
            print(f"You guessed {guessed_letter}, that's not in the word. Get ready to say good bye to your headd...!")
        elif nr_lives == 4:
            print(f"You guessed {guessed_letter}, that's not in the word. Too baddd !! Too baddd !!")
        elif nr_lives == 3:
            print(f"You guessed {guessed_letter}, that's not in the word. Let's say good byee to your right armm.. !!")
        elif nr_lives == 2:
            print(f"You guessed {guessed_letter}, that's not in the word. The hangman is waiting for you, choose carefully!!")
        elif nr_lives == 1:
            print(f"You guessed {guessed_letter}, that's not in the word. One last letter could save you... or finish you!")
    else:
        is_guessed = False
        print(random.choice(cursed_phrase_list))


    
    if is_victory(blank):
        print(HANGMANPICS[7-nr_lives])
        print(blank_str)
        print("You win!")
        break
    print(HANGMANPICS[6-nr_lives])
    print(blank_str)

if nr_lives <= 0 :
    print("#####################################################################")
    print(f"YOU ARE DEADDD ... ! Game Over! The word is {keyword}. Hahaha Stupid!")
    print("#####################################################################")