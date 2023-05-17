# prints no lines, letters, words

# with open("test.txt", "r") as file:
#     nLines = 0
#     nWords = 0
#     nLetters = 0
#     for line in file:
#         nLines += 1
#         words = line.split(" ")
#         nWords += len(words)
#         for word in words:
#             nLetters += len(word)


# print(nLines, nWords, nLetters)
    
    
# read file in chunk
# with open("test.txt", "r") as file:
#     size_of_chunk = 15
#     file.seek(28)
#     print(file.tell())
#     chunk = file.read(size_of_chunk)
#     print(chunk)
    

# file.seek(10) to move cursor
# file.tell() to know where cursor is at
# file.read(value) to read from cursor_position to cursor_position + value
# file.readlines() to read entire file at once





# with open("test.txt", "r") as file:
#     fruits = []
#     for line in file:
#         line = line[3:-1]
        
#         if "," in line:
#             entry = line.split(", ")
#         else:
#             entry = line

#         fruits.append(entry)

# print(fruits)


# find out which fruits are mentioned how many times
# hint maintain fruits and numbers list (2 list)


with open("test.txt", "w") as f:
    f.write("Test")
    f.seek(100)
    f.write("B")


# copying

with open("myfile.zarif", "wb") as file_child:
    file_child.write(bytes("My name is zarif", "utf-8"))


    

# INSERT INTO "user" VALUES ('zikram', 'zarifikram003@gmail.com', '1234', 'https://i.picsum.photos/id/980/200/200', '2000-05-29', 'male', 'Zarif', 'Ikram', 'Dhanmondi 9/a Dhaka', 'Fun', 'Messy', 'Guessy', 'Student');