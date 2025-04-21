# method 1: to open a file

file = open("my_file.txt")
contents = file.read()
print(contents)
file.close()


# method 2:

with open("my_file.txt") as file:
    contents = file.read()
    print(contents)
    file.close()

# write into a file with append mode
with open("my_file_1.txt", 'a') as file:
    file.write("Hello world")