# Tyler Ruoff

def my_function1(lst):
    """
    Doubles each number in the list and returns
    the list.
    """
    return [x+x for x in lst]

def my_function2(lst):
    """
    Takes in a lst and returns whatever is stored
    in the last index.
    """
    return lst[-1]

lst1 = [0,1,2,3]
print(my_function1(lst1))
print(my_function2(lst1))

lst2 = [9,2,3,40]
print(my_function1(lst2))
print(my_function2(lst2))

lst3 = [3,1,2]
print(my_function1(lst3))
print(my_function2(lst3))