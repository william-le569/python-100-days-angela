# import prettytable
# x = prettytable.PrettyTable()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("pokemon name".title(), ["Pikachu", "Squirtle", "Charmander"])
table.add_column("type".title(), ["Electric", "Water", "Fire"])
table.align = "l"

print(table)