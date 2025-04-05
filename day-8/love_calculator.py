def calculate_love_score(name1, name2):
    score1 = 0
    score2 = 0
    name1 = name1.lower()
    name2 = name2.lower()
    name3 = name1 + name2
    for char in name3:
        if char == 't' or char == 'r' or char == 'u' or char == 'e':
            score1 += 1
        if char == 'l' or char == 'o' or char == 'v' or char == 'e':
            score2 += 1
    print(score1*10 + score2)
            
calculate_love_score("Kanye West", "Kim Kardashian")