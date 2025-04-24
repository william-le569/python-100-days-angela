# import pandas as pd

# with open("file1.txt") as file:
#     file_1_list = file.readlines()

# with open("file2.txt") as file:
#     file_2_list = file.readlines()

# result = [int(number_1.strip()) for number_1 in file_1_list for number_2 in file_2_list if number_1 == number_2]

# # Eliminate duplicate

# seen = set()
# no_duplicates = []
# for item in result:
#     if item not in seen:
#         seen.add(item)
#         no_duplicates.append(item)

# result = no_duplicates

# print(result)


# -------- Solution ----------------

with open("file1.txt") as file1:
  list1 = file1.readlines()
    
with open("file2.txt") as file2:
  list2 = file2.readlines()
    
result = [int(num) for num in list1 if num in list2]
 
print(result)

