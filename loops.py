# loop depends on a condition
# we DO NOT want infinite loops 
# THE FOR LOOP

# a for loop has a starting point and an ending point

# range is the function for defining a starting point and ending point

# for i in range(0, 5):
#     print(i)


# range also takes one optional variable called step
# for i in range(0, 15, 3):
#     print(i)


# loops can be nested

# for i in range(0, 10):
#     for j in range(0, 5):
#         print("value of i : " + str(i) + "\n value of j : " + str(j) + "\n\n")



# sum = 0

# # 1 + 2 + 3 + 4 + ... + n
# n = int(input())
# for i in range(1, n + 1):
#     # sum = sum + i
#     sum += i

# Write a program in python to find the sum of series X^0/0! - X^2/2! + X^4/4!-.... upto nth term
# input: n = 1 x = 1 output = 1
# input: n = 2 x = 1 output = 1/2 

# n = int(input("n : "))
# x = int(input("x : "))

# numerator = 1
# denominator = 1
# ans = 0

# for i in range(0, n):
#     # numerator = (-1*x) ** i  # for i = 1 numerator = -x
#     # numerator *= x**i # for i = 1 numertor = -x**2
#     numerator = ((-1)**i) * x**(2*i)
    
#     ans += numerator/denominator
#     print(str(numerator) + " / " + str(denominator) + " = " + str(ans))
#     denominator *= (2*i + 1)  #when i = 0 denominator = 1. So 2*i + 1 = 1 so, updated denom = 1*1 = 1
#     denominator *= (2*i + 2)   # when i = 0 denom = 1. So 2*i + 2 = 2 so, updated denom = 2*1 = 2!

# Write a program in python to find the sum of the series 1 + 1/2^2 + 1/3^3 + ..+ 1/n^n

# break
# continue

# BREAK
# print('break example')
# for i in range(0, 10):
#     print(i)
#     if i == 5:
#         print("time to get out")
#         break

# CONTINUE
# print("continue exampmle")
# for i in range(0, 10):
#     print(i)
#     if i >= 5:
#         print("time to get out")
#         continue
        # will skip the later part of the loop and go to next iteration
    # print(i)


# string find function manually
# random_string = "abcdefcgh"
# random_char = "c"
# ans = -1

# for i in range(len(random_string)):
#     if random_string[i] == random_char:
#         ans = i
#         print("found it")
#         # break

# print("ans" + str(ans))

# Write a program in python to find prime number within a range.
# example l = 10, r = 30
# output : 11, 13, 17, 19, 23, 29

# Write a program in python to find the sum of digits of a given number.
# example number = 10101010110101010101010101010
# output = 15

# input = 5
# *
# **
# ***
# ****
# *****

# input = 7
# *
# **
# ***
# ****
# *****
# ******
# *******

# while
# a = 10
# while a > 0:  #while a is positive
#     print(a)
#     a -= 1

# for
# for i in range(10, 0, -1):
#     print(i)

# for loop is useful for getting a value repeatedly
# while loop is useful for checking a condition repreatedly

password = "this is a very complicated password"

# user_input = input("type in the password:       ")

# while not user_input == password:
#     print("WRONG PASSWORD")
#     user_input = input("type in the password:       ")

# print("welcome user!")

# if user gives password let them in. And stop asking
# incorrect password say "wrong pass"
# if chance > 5 "say no more chance" and stop asking
# chance = 0
# while True:
#     chance += 1
#     user_input = input("type in the password:       ")
#     if user_input == password:
#         print("welcome!!!")
#         break
#     else:
#         print("wrong password")
#         if chance > 4:
#             print("no more chance")
#             break



# min finding problem
# take an input n from user
# take n numbers from users
# find out their min

# 5
# 10 4 6 1 -61
# output = -61