# try: 
#     num = input()
#     print("You entered: " + str(num))   #input automatically makes it a string
#     num = int(num)
#     num +=1
#     print(num) 
# except:
#   input("you did not enter a number")

"""
Opening a file
"""
# with open('movies.txt') as file:
#     for line in file:
#         print(line.strip())

# name = "Bob"
# print(f"Hi there {name}")
# print("Hi there", name)
# hello = f'Hello, my friend {name}'
# print(hello)
heights = {}
with open('heights.txt') as file:
    for line in file:
        line = line.strip()
        values = line.split()
        heights[f"{values[0]} {values[1]}"] = int(values[2])
    print(heights)