def most_popular_foods(fav_foods):

    '''
    Given a dictionary of people's favorite foods, return a new dictionary
    with food as the key and the list of people who like that food as the value.
    Example, given 
    fav_foods={'Kathleen': 'pizza', 'Steve': 'burger', 'John': 'steak', 
    'Michelle': 'pasta', 'Patrick': 'pizza'})
    You should return the new dictionary 
    {'pizza': ['Kathleen', 'Patrick'], 'burger': ['Steve'], 'steak': ['John'], 
    'pasta': ['Michelle']}

    '''
    newdict = {}
    for name,fav_food in fav_foods.items():
        if fav_food not in newdict:
            newdict[fav_food] = []
        newdict[fav_food].append(name)
    return newdict




    


assert most_popular_foods(fav_foods={'Kathleen': 'pizza', 'Steve': 'burger', 'John': 'steak', 'Michelle': 'pasta', 'Patrick': 'pizza'}) == {'pizza': ['Kathleen', 'Patrick'], 'burger': ['Steve'], 'steak': ['John'], 'pasta': ['Michelle']}, "expected {'pizza': ['Kathleen', 'Patrick'], 'burger': ['Steve'], 'steak': ['John'], 'pasta': ['Michelle']}"
print("correct")
assert most_popular_foods({"Kathleen": "pizza", "Yin": "pizza", "Kearicia":"Italian","Owen": "burgers"}) == {'pizza': ['Kathleen', 'Yin'], 'Italian': ['Kearicia'], 'burgers': ['Owen']}, "expected {'pizza': ['Kathleen', 'Yin'], 'Italian': ['Kearicia'], 'burgers': ['Owen']}"
print("correct")
assert most_popular_foods({'Kathleen': 'pizza', 'Max':'burgers', 'Matt':'burgers', 'Andy':'pizza','Christina':'burgers'}) == {'pizza': ['Kathleen', 'Andy'], 'burgers': ['Max','Matt','Christina']}, "expected {'pizza': ['Kathleen', 'Andy'], 'burgers': ['Matt','Max','Christina']}"
print("correct")



















'''
Steps
    Create an empty dictionary
    Iterate through the fav_foods dictionary
        if the food is NOT in the new dictionary:
            create an empty list and add the person to the list
            add the food as they key and the list as the value
        else:
            add the person to the list of people who favorite that food
    return dictionary
'''