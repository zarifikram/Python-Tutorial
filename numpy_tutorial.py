from random import random
import numpy as np

# turn a list into numpy
# random_list = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
# random_numpy_list = np.array(random_list)

# print(random_list)
# print(random_numpy_list.shape)

# creating a diagonal matrix
# diagonal_matrix = np.eye(4)
# print(diagonal_matrix)

# create a list filled zeros
# matrix = np.zeros((5, 4))
# print(matrix)

# create a list filled w ones
# matrix = np.ones((2, 5))
# print(matrix)
# for i in range(matrix.shape[0]):
#     for j in range(matrix.shape[1]):
#         matrix[i][j] = int(input())

# print(matrix)

# matrix = matrix + 5
# print(matrix)

# 2
# 3
# 1
# 2
# 3
# 4
# 5
# 6
# OUTPUT
# 1 2 3
# 4 5 6
# 3
# 1
# 1
# 2
# 3
# OUTPUT
# 1
# 2
# 3

# OUTPUT
# TBD
# TBD

# Matrix Multiplication

# nRow, nCol = input('Row, Column : ').split(",")
# nRow = int(nRow)
# nCol = int(nCol)

# matrix1 = np.ones((nRow, nCol))
# for i in range(nRow):
#     for j in range(nCol):
#         matrix1[i][j] = int(input())


# nRow, nCol = input('Row, Column : ').split(",")
# nRow = int(nRow)
# nCol = int(nCol)

# matrix2 = np.ones((nRow, nCol))
# for i in range(nRow):
#     for j in range(nCol):
#         matrix2[i][j] = int(input())




# resultant_matrix = np.ones((matrix1.shape[0], matrix2.shape[1]))

# for i in range(matrix1.shape[0]):
    # for j in range(matrix2.shape[1]):
        # sum = 0
        # resultant_matrix[i][j] = matrix1[i, :].dot(matrix2[:, j])
        # for k in range(matrix1.shape[1]):
        #     sum += (matrix1[i][k] * matrix2[k][j])

        # resultant_matrix[i][j] = sum

# using np function
# resultant_matrix = matrix1.dot(matrix2)
# print(matrix1)
# print(matrix2)
# print(resultant_matrix)

# operations in numpy
# a = np.ones(5)
# b = np.ones(5)

# for i in range(5):
#     a[i] = int(input())

# for i in range(5):
#     b[i] = int(input())


# print(a)
# print(b)
# print(a + b)


# numpy diagonal matrix with user specified values
# print(np.diag([2, 3, 1, 10]))

# creates a list with 5 entries with numbers from 1 to 100
# a_list_with_ints = np.random.randint(1, 100, 5)
# creates a list with 5 entries from 0. to 1.
# a_list_with_floats = np.random.rand(5)
# cretes a list with 5 entries with floats (-ve including)
# a_list_with_negative_floats = np.random.randn(5)
# print(a_list_with_negative_floats)

# reshaping
# a = np.random.randint(1, 10, 8)
# a = a.reshape((2, 4))
# reshaping with -1 takes away the calculation
# a = a.reshape((2, -1))
# print(a)

# create a 10 X 5 matrix that has values from 0. to 10.

# astype changes the type of the list
# a = np.random.rand(5)
# print(a)
# a = a.astype("int32")
# print(a)

# create a random list that has zero in the last row and last column
# random_list = np.random.rand(16).reshape((4,-1))
# print(random_list)
# random_list[3] = 0
# random_list[:, 3] = 0
# print(random_list)
# create a list that looks like this

# 1 0 0 0 
# 1 1 0 0
# 1 1 1 0
# 1 1 1 1

# replace 1 with random number
# random_list = np.random.rand(16).reshape((4,-1))
# for row_no in range(random_list.shape[0]):
#     random_list[row_no, row_no + 1 : ] = 0

# print(random_list)


# Random Password Generator
# user will give you length
# for that length generate a password that
# i) includes alphabet (upper + lower)
# ii) includes number
# iii)includes special symbols

# import random

# alphabets_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# alphabets_lower = alphabets_upper.lower()
# numbers = "1234567890"
# symbols = "@#$%^&*()_+-="
# characters = alphabets_lower + alphabets_upper + numbers + symbols

# length_of_password = int(input("length :        "))
# # 8
# password_list = []
# upper_char = alphabets_upper[random.randint(0, len(alphabets_upper) - 1)]
# password_list.append(upper_char)
# lower_char = alphabets_lower[random.randint(0, len(alphabets_lower) - 1)]
# password_list.append(lower_char)
# number_char = numbers[random.randint(0, 9)]
# password_list.append(number_char)
# symbol_char = symbols[random.randint(0, len(symbols) - 1)]
# password_list.append(symbol_char)

# characters_indices = np.random.randint(0, len(characters) - 1, length_of_password - 4)
# for character_index in characters_indices:
#     password_list.append(characters[character_index])


# np.random.shuffle(password_list)
# password = "".join(password_list)
# print(password)



# USING NUMPY CONDITIONS
# you will get a numpy list of integers
# create a new list from that list where every value is greater than 10

# random_list = np.random.randint(0, 50, 10)

# print(random_list)
# # print(random_list > 10)
# # print(random_list[[False, True, False, True]])
# # print(random_list[random_list > 10])

# print(random_list[])

# get a list
# create another list from that which only has the even values
# random_list[random_list % 2 == 0] = 0
# print(random_list)

# creating a list
# random_list = np.linspace(10, 20, 10)
# print(random_list)

# random_list = np.arange(10, 20, 2)
# print(random_list)

# a = np.arange(10, 15, 3)
# b = np.linspace(10, 15, 7)

# print(a, b)

# special function
arr = np.random.randint(-15, 15, 15).reshape((3, -1))
print(arr)
# print(np.sum(arr))
# print(np.min(arr, axis = 1))
# print(np.max(arr))
# print(arr.sum())
# print(np.sum(arr, axis = 1))
# for row wise sum, think of what changes. Column is what is changing. So, axis = 1
# row = 0, column = 1,
# print(np.cumsum(arr, axis = 1))

# some math functions
# print(np.sin(arr))

# np.sin
# np.cos
# np.pi
# np.sqrt
# np.tan
# np.asin
# np.acos

# print(np.argmax(arr, axis = 1))



