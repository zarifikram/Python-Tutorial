# key - value
# tree binary hash key 
# mutable

# initialize



# random_dictionary = {"name" : "zarif", "age" : 22, "location" : "dhaka"}
random_dictionary = dict(name = "zarif", age = 22, location = "dhaka")

# modify
# if "nme" in random_dictionary:
    # random_dictionary.pop("nme")
# random_dictionary.popitem()
# print(random_dictionary)

# random_dictionary["name"] = "ikram"
# print(random_dictionary)

# random_dictionary2 = dict(random_dictionary)
# random_dictionary2 = random_dictionary.copy()
# random_dictionary2["name"] = "iasfasfsaf"
# print(random_dictionary)


# access
# print(random_dictionary["location"])

# for key in random_dictionary.keys():
#     print(key)

# for value in random_dictionary.values():
#     print(value)

# print(random_dictionary.values())

# for key, value in random_dictionary.items():
#     print(key, " ", value)


# name
# age
# salary
# club

# list_of_dictionary = []
# list_of_dictionary.append(random_dictionary)
# print(list_of_dictionary)

# update
# random_dictionary2 = {"name" : "ikram", "age" : 1000, "id": 100034}
# print(random_dictionary2 | random_dictionary)

# random_dictionary2 = {3 : 10, 1: 10, 0 : 124, 2 : 214}
# print(random_dictionary2)

# names = ["asfb", "afs", "adf", "adfa"]
# salary = [1000, 124121, 1241, 1241]

# salary_dictionary = {names[i] : salary[i] for i in range(4)}

# print(salary_dictionary)


# takes input of cities and temperature of that city (in c)
# make a dictionary from those inputs
# make another dictionary from the first one but for farenheight
# create another dictionary which has tempartures greater than 70F
# return these three dictionaries