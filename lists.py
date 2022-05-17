# # initalizing a list
# random_list = []
# print(type(random_list))

# list with items

# # type them out
# random_list = ["10", "12", 51]
# print(random_list)

# append
# random_list = [10, 15]
# random_list.append(51)

# list also supports multiple types
# random_list.append("15")
# print(random_list)

# extend
# random_list = [10, 15, 152]
# random_list2 = [1, 2]
# APPEND DOESNOT MATTER
# random_list.append(random_list2)
# print(random_list)
# print(len(random_list))

# ENTEND DOES
# random_list.extend(random_list2)
# print(random_list)
# print(len(random_list))


# insert
# random_list = [1, 2, 3, 5]
# random_list.insert(3, 4)
# print(random_list)

# using list access operator
# random_list = [10, 152, 12]
# random_list[1] = 1
# print(random_list)


# slicing
# random_list = [10, 1252, 1, 5, 15, 0 , 125, 25]
# print(random_list[::-1])

# reverse()

# random_list = [10, 1252, 1, 5, 15, 0 , 125, 25]
# random_list.reverse()
# print(random_list)

# in-place functions : functions that change the object entirely

# problem : take input from user until user gives you 0. If the user inputs positive numbers, add them in a list called positives, if negative, add them in a list called negatives
# example:
# 10 -15 5 -5 -1 2 5 0
# postives : [10, 5, 2, 5]
# negatives : [-15, -5, -1]

# remove() 
# random_list = ["red", "blue", "brown", "orenge"]
# print(random_list)
# random_list.remove("blue")
# # MAKE SURE IT IS IN THE LIST BEFORE WE REMOVE IT, OTHERWISE WILL GET AN ERROR
# print(random_list)

# if "blue" in random_list:
#     random_list.remove("blue")
# else:
#     print("it is not found")

# pop()
# random_list = [1, 2, 3, 4, 15]
# removed_item_index = random_list.pop()
# print(random_list)
# print(removed_item_index)

# sort()



# random_list = [14, -4, 5, 1, 125, 10]
# random_list_sorted = [-4, 1, 5, 10, 14, 125]
# random_list_2 = random_list.sort(reverse=True)
# print(random_list)
# print(random_list_2)

# random_list_2 = sorted(random_list, reverse=True)
# print(random_list)
# print(random_list_2)

# simple phonebook problem
# user will type name and phonenumber


# commands:
# "add" : asks name and phonenumber and adds to the list
# "remove" : asks name and remove from the list
# "sort-a" : sorts in accending order
# "sort-d" : sorts in descending order
# "show" : show all items in list in this format : "name"         :   "phonenumber"

# add zarif 1234
# > ["zarif-1234"]
# add ikram 1245
# > ["zarif-1234", "ikram-1245"]
# sort-A
# > ["ikram-1245", "zarif-1234"]
# remove zarif
# > ["ikram-1245"]
# show
# > ["ikram-1245"]


# "10-20-40-10-40"
# [10, 20, 40, 10, 40]


#"10   40   10   50   -20"
# [10, 40, 10, 50, -20]

# basic
# seperator = "-"
# user_input = "10-20-40-10-40"
# output_list = []

# while True:
#     seperator_index = user_input.find(seperator)

#     if seperator_index == -1:
#         list_item = int(user_input)
#         output_list.append(list_item)
#         break

#     list_item = int(user_input[:seperator_index])
#     output_list.append(list_item)
#     user_input = user_input[seperator_index + 1 : ]


# print(output_list)

# print(user_input.split(" "))

# user_input = "asdfsa asf sdf sfsf fafsas dfafsdfas asf asdfas asfa sdaf a asdf af adfafsaf afasfs sfaf adfaasf asfdsf asfafsd safasf adfasfa"
# words = user_input.split(" ")
# print(f"no of words :   {len(words)}")


# ["10", "40", "10", "50", "-20"]
#"10   40   10   50   -20"

# input_list = ["10", "40", "10", "50", "-20"]
# persed_string = ' - '.join(input_list)
# print(persed_string)

# You will be given a sentence. Return another sentence but the words will be alphabetically sorted (use sorted/.sort())

# "Marry had a little lamb"
# "a had lamb little Marry"

# list_of_items = ["orenge", "banana", "apple", "pineapple"]
# string_of_items = ""

# for each loop
# for item in list_of_items:
    # do things with item


# for index, item in enumerate(list_of_items, start=5):
#     print(index, "  ", item)


# adjacent graph
# adjacent_graph = [
#     [1, 2, 4],
#     [0, 2, 3],
#     [0, 1],
#     [1],
#     [0]
# ]

# find out 0's neightbors
# adjacent_graph[0]
# find out if 1 is 0's neightbor
# if 1 in adjacent_graph[0]

# user will input n
# for n lines, user will give u and v, where u and v are neighbors

# 5
# 0 1
# 1 2
# 0 2
# 1 3
# 0 4

# OUTPUT
# adjacent_graph = [
#     [1, 2, 4],
#     [0, 2, 3],
#     [0, 1],
#     [1],
#     [0]
# ]

# [
#   [],
#   [],
#   [],
#   [],
# ]

# string_random = "a"*5 

# list_random = [[]] * 5
# print(list_random)


# nested list

# takes user input n
# n = int(input("Give the number of edges:    "))
# make a list with n empty lists inside
# adjacency_list = [ [] ] * n

# reference to an object is the memory location where it is stored


# adjacency_list = []
# for i in range(n):
#     adjacency_list.append([])

# print(adjacency_list)

# # take u and v for n times
# for i in range(n):
#     u = int(input("u :      "))
#     v = int(input("v :      "))
#     (adjacency_list[u]).append(v)
#     (adjacency_list[v]).append(u)
  
# print(adjacency_list)

# 5
# A B C D E

# 4
# A B
# D E
# B C
# B D

# B
# OUTPUT
# A : 1st
# C : 1st
# D : 1st
# E :  Not 1st


# take number of users
# take the name of users
# n_users = int(input())
# names = []
# names_to_numbers = {}
# for i in range(n_users):
#     name = input("Input name:       ")
#     names.append(name)
#     names_to_numbers[name] = i

# # take the number of connections
# n_connections = int(input('Enter the number of connections'))
# adjacency_list = []
# for i in range(n_users):
#     adjacency_list.append([])

# # take the connections
# for i in range(n_connections):
#     first_name = input("Enter the first name: ")
#     second_name = input("Enter the second name: ")
#     u = names_to_numbers[first_name]
#     v = names_to_numbers[second_name]

#     adjacency_list[u].append(v)
#     adjacency_list[v].append(u)

# # take the name
# given_name = input("Input the user name:    ")

# for name in names:
#     if name == given_name:
#         continue    #do not do anything
    
#     # name is not give_name if we reach this point
#     given_name_neighbors = adjacency_list[names_to_numbers[given_name]]
#     is_first = names_to_numbers[name] in given_name_neighbors
#     yes = "1st"
#     no = "not 1st"
#     print(f"{name} : {yes if is_first else no}")

    


# Write a Python program to remove duplicates from a list.
# [10, 40, 10] => [10, 40]
# Write a Python program to convert a list of characters into a string.
# ["a", "b", "c"] => "abc"
# Write a python program to check whether two lists are circularly identical.
# [10, 20, 30], [20, 30, 10] > Identical
# [10, 20, 30], [10, 30, 20] > not identical
# Write a Python program to find the second largest number in a list.
# [10, 20, 30, 40] > 30


# Write a python program to check whether two lists are circularly identical.
# [10, 20, 30], [20, 30, 10] > Identical
# [10, 20, 30], [10, 30, 20] > not identical



# list_1 = [10, 20, 30, 40, 50]
# list_2 = [40, 30, 50, 10, 20]


# list_1 0 list_2 (0 + 1) % 5
# list_1 1 list_2 (1 + 1) % 5
# list_1 2 list_2 (2 + 1) % 5
# list_1 3 list_2 (3 + 1) % 5


# constant = 3
# length = len(list_1)
# for constant in range(5):
#     is_identical = True
#     for index, value in enumerate(list_1):
#         if list_2[(index + constant) % length] != value:
#             is_identical = False

#     if is_identical:
#         break

# print("" if is_identical else "not ", "circularly identical")

list_1 = [10, 30, 40, 50, 20]

max_number = list_1[0]

for number in list_1:
    if number > max_number:
        max_number = number

list_1.remove(max_number)

second_max_number = list_1[0]

for number in list_1:
    if number > second_max_number:
        max_number = number

print(second_max_number)