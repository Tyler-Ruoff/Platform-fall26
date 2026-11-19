print("Hello world!")

# this is a comment

'''
multi line commemt
(usually describes a function)

'''

# highlight words and do (command /)

x = 100
print(x)
x=5.5
print(x)
# you can change the type of a variable (can make the same variable an int, float, etc. with no error)
x = 100
y = 10
print(int(x/y))
print(x//y)
if x<0:
    print("x is less than 0")
else:
    print("x is not less than 0")
    i = 0
    # creating list and iterating thru it
nums = [0,1,2,3,4,5]
for i in range(len(nums)):
    print(i, nums[i])

print("\t")
for i in range (len(nums)-1, -1, -1):
    print(i, nums[i])
print("\t")
for i, val in enumerate(nums):    # STUDYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
    print(i, val)

