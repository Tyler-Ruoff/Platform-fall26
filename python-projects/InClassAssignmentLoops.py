# loops in class assignment (week 1 lecture 2)

# All numebrs divisible by 3 from 0-20:
for i in range(0,21, 3):
    print(i)

# Write a while loop that calculates the sum of all even numbers between 1 and 50 (inclusive). Print the result.
sum = 0
for i in range(1, 51):
    sum += i
print(sum)

# You are given a list of numbers:
# numbers = [5, 8, 2, 15, 10, 3, 7]
# Use a for loop to print the numbers greater than 5.
print("Excercise 3: \n")
numbers = [5, 8, 2, 15, 10, 3, 7]
for num in numbers:
    if num > 5:
        print(num)
print()


# You are given a list of numbers:
# numbers = [1,2,3,4,5]
# Create a new list that stores a running sum of numbers. The running sum list should hold the values:
# [1,3,6,10,15].
print("challenge: \n")
numbers = [1,2,3,4,5]
j = [1]
for i in range(len(numbers)-1):
    j.append(j[i] + numbers[i+1])
print(j)


def swap(lst):
    first = lst[0]
    lst[0] = lst[len(lst)-1]
    lst[len(lst)-1] = first
    print(lst)

swap(numbers)

full = "Tyler Reece Ruoff"
first = full[:5]
middle = full[6:12]
last = full[12:]
first_char = full[0]
last_char = full[-1]
print(full, first, middle, last, first_char, last_char)