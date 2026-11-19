# Tyler Ruoff
# Cite any sources you used to help with the homework 
# including TAs and classmates

def exchange(str):
    # Checks to see if the new string
    # can work with its length. Then it
    # creates a new string using new pieces
    # of the old one that fits the requirments

    if (len(str) < 2):
        return str
    return str[-1] + str[1:-1] + str[0]


def remove_range(alist, min, max):
    # Returns a list of numbers that are
    # not between the min and max

    return [x for x in alist if ((x>max) or (x<min))]


def word_count_in_set(words):
    # makes the list a set which automatically
    # gets rid of duplicates. Then counts the length
    # which returns the total number of unique words
    return len(set(words))


def topping1(dictionary):
    # Checks to see if ice cream is in the dictionary
    # yet. If not, it set cherry to ice cream. Returns that
    # plus bread as the key for butter which should happen
    # in all of the runs.

    if (dictionary.get('ice cream') != None):
        dictionary['ice cream'] = 'cherry'
    dictionary['bread'] = 'butter'
    return dictionary


def word_count(strings):
    # turns the list into a set which automatically gets rid
    # of the duplicates. For each non-duplicated word, it finds
    # the count of that word in the original list and sets
    # its value to the amount of times it appears in the list
    return {num : strings.count(num) for num in set(strings)}


def friend_list(friend_dictionary):
    # Checks to see if the key already exists in the dictionary.
    # If not, it sets the key to a list. Lastly, it appends the 
    # names that appear to eachother in the values and returns
    # the dictionary.
    j = {}
    for name1, name2 in friend_dictionary.items():
        if (j.get(name1) == None):
            j[name1] = []
        if (j.get(name2) == None):
            j[name2] = []
        j[name1].append(name2)
        j[name2].append(name1)
    return j


# Test functions
assert exchange("code") == "eodc", 'exchange("code") expected eodc'
print("correct")
assert exchange("ba") == 'ab', 'exchange("ba") expected ab'
print("correct")
assert exchange("a") == 'a', 'exchange("a") expected a'
print("correct")

assert remove_range([7, 9, 4, 2, 7, 7, 5, 3, 5, 1, 7, 8, 6, 7], 5, 7) == [9, 4, 2, 3, 1, 8] , '[9, 4, 2, 3, 1, 8] expected'
print("correct")
assert remove_range([7, 9, 4, 7, 7, 5, 5, 1, 7, 8, 6, 7], 2, 3) == [7, 9, 4, 7, 7, 5, 5, 1, 7, 8, 6, 7], '[7, 9, 4, 7, 7, 5, 5, 1, 7, 8, 6, 7] expected'
print("correct")
assert remove_range([7, 9, 7], 7, 9) == [], '[] expected'
print("correct")

assert word_count_in_set(["the", "quick", "brown", "fox", "brown"]) == 4, 'expected 4'
print("correct")
assert word_count_in_set(["brown", "brown"]) == 1, 'expected 1'
print("correct")

assert topping1({"ice cream": "peanuts"}) == {"bread": "butter", "ice cream": "cherry"}, 'expected {"bread": "butter", "ice cream": "cherry"}'
print("correct")
assert topping1({"bread": "butter"}) == {"bread": "butter"}, 'expected {"bread": "butter"}'
print("correct")
assert topping1({"pancake": "syrup"}) == {"bread": "butter", "pancake": "syrup"}, '{"bread": "butter", "pancake": "syrup"}'
print("correct")

assert word_count(["a", "b", "a", "c", "b"]) == {"a": 2, "b": 2, "c": 1}, 'expected {"a": 2, "b": 2, "c": 1}'
print("correct")
assert word_count(["c", "b", "a"]) == {"a": 1, "b": 1, "c": 1}, 'expected {"a": 1, "b": 1, "c": 1}'
print("correct")
assert word_count(["c", "c", "c", "c"]) == {"c": 4}, 'expected {"a": 1, "b": 1, "c": 1}'
print("correct")

assert friend_list({"Marty": "Cynthia", "Danielle": "Marty"})== {"Cynthia":["Marty"], "Danielle":["Marty"], "Marty":["Cynthia", "Danielle"]}, 'expected {"Cynthia":["Marty"], "Danielle":["Marty"], "Marty":["Cynthia", "Danielle"]}'
print("correct")


# Problems found on https://codingbat.com/python
