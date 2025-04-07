enemies = 1

def increase_enemies():
    enemies = 2
    print(enemies)

print("output first case:")
increase_enemies()
print(enemies)

# output first-case:
# 2
# 1

enemies = 1

def increase_enemies():
    global enemies
    enemies = 2
    print(enemies)

print("output second case:")
increase_enemies()
print(enemies)

# output second-case:
# 2
# 2
