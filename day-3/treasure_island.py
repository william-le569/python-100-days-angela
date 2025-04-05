print('''
                         /\          /\\
                         ( \\        // )
                          \ \\      // /
                           \_\\||||//_/
                            \/ _  _ "
                           \/|(O)(O)|
                          \/ |      |
      ___________________\/  \      /
     //                //     |____|
    //                ||     /      \\
   //|                \|     \ 0  0 /
  // \       )         V    / \____/
 //   \     /        (     /
""     \   /_________|  |_/
       /  /\   /     |  ||
      /  / /  /      \  ||
      | |  | |        | ||
      | |  | |        | ||
      |_|  |_|        |_||
       \_\  \_\        \_\\ Hard'96   
      
      ''')

print("Welcometo Treasure Island.\n Your mission is to find the treasure")
choice1 = input('Type "left" or "right": ').strip().upper()

game_over_message = "Game Over!"
win_message = "You win!"

if choice1 == 'R' or choice1 == "RIGHT":
    print(game_over_message)
elif choice1 == "L" or choice1 == "LEFT":
    choice2 = input("Swim or Wait: ").strip().upper()

    if choice2 == "SWIM":
        print(game_over_message)
    elif choice2 == "WAIT":
        choice3 = input("You choose which door? Red or Green or Blue: ").strip().upper()

        if choice3 == "RED" or choice3 == "BLUE":
            print(game_over_message)
        elif choice3 == "GREEN":
            print(win_message)
        else:
            print(game_over_message)
    else:
        print(game_over_message)
else:
    print(game_over_message)