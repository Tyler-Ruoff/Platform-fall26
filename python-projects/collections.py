lst = [10,20,30,40,50]
lst.append(5)
lst.append(6)
lst.append(7)
print(lst)


del lst[-1]
lst.remove(50)
print(lst)

lst.sort()

lst.reverse()

newlst = lst[0:1]

print(newlst)

lst.append(20)

count20 = lst.count(20) # counts how many of the parameter are in the list

index20 = lst.index(20) # tells you what the index of the parameter in the list is


cpylst=lst     # This does not copy the list
cpylst[0] = 999
print(lst)
print(cpylst)

cpylst = lst.copy()   # actually copies the list
cpylst=lst[1:]  # also copies the list

empty = []
print(empty)


lst = [999,10,20,30,40,20,20]
empty = []
for num in lst:
    if ((num<=50) and (num>=20)):
        empty.append(num)
print(empty)


squares=[]


for i in range(1,10):
    squares.append(i*i)
print(squares)

for i,val in enumerate(squares):
    print(i+1,val)

square = [x*x for x in range(1,9)]
print(square)
newlst = []

odd_nums = [1 for num in lst if ((num<=50) and (num>=20))]
print(odd_nums)

# sets
aset = set()
aset = {1,2,3,4,3,2,1}
print(aset)
aset.add(0)
print(aset)  # uses add and not append

# print(aset[0]) is not possible

# dictionary instead of hashmap

# dictionary = {}

# dictionary['key'] = 'hi'

fav_foods = {'Tyler':'Sushi', 'Kathleen':'pizza','Frank':'beverage guy'}

food = fav_foods['Kathleen']
print(food)

if 'bob' in fav_foods:
    print(fav_foods['bob'])
else:
    fav_foods['bob'] = 'Ice Cream'
print(fav_foods)

for name,fav_food in fav_foods.items():
    print(name,":",fav_food)