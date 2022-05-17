# k = int(input("Input the number of values you want to add :     "))

# sum = 0

# for i in range(k):
#     x = int(input(f"Input integer#{i + 1} :     "))
#     if x < 0:
#         print("Don't input negative numbers!")
#         continue

#     sum += x
    
# print(f"The sum is {sum}")


n = int(input("Input an integer"))

# for i in range(n):
#     line = ""
#     for j in range(i + 1):
#         line += "*"

#     print(line)

for i in range(n):
    for j in range(i + 1):
        print(" "*(n - j)+"*"*(2*j + 1))
