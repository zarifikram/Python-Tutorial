import numpy as np


playerNames = np.array([]).astype("str")
playerAges = np.array([]).astype("int32")
playerSalaries = np.array([]).astype("float64")
playerClubs = np.array([]).astype("str")

# define some more lists 

with open("playerDatabase.txt", "r") as file:
    lines = file.readlines()
    playerNames = np.array(lines[0][:-1].split(",")).astype("str")
    playerAges = np.array(lines[1][:-1].split(",")).astype("int32")
    playerSalaries = np.array(lines[2][:-1].split(",")).astype("float64")
    playerClubs = np.array(lines[3][:-1].split(",")).astype("str")
    
        

while(True):
    command = input()

    if command == "quit":
        break
    elif command == "add":
        name = input()
        age = int(input())
        salary = float(input())
        club = input()
        
        playerNames = np.append(playerNames, name)
        playerAges = np.append(playerAges, age)
        playerSalaries = np.append(playerSalaries, salary)
        playerClubs = np.append(playerClubs, club)

        with open("playerDatabase.txt", "w") as f:
            f.write(",".join(playerNames) + "\n")
            f.write(",".join([str(age) for age in playerAges]) + "\n")
            f.write(",".join([str(salary) for salary in playerSalaries]) + "\n")
            f.write(",".join(playerClubs) + "\n")


    elif command == "print":
        for ind, value in enumerate(playerNames):
            print(f"Name : {playerNames[ind]}")
            print(f"Age : {playerAges[ind]}")
            print(f"Salary : {playerSalaries[ind]}")
            print(f"Club : {playerClubs[ind]}")
            print()