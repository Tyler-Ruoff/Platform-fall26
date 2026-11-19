string = "jjjmmmm"
last_4_doubled(string)
def last_4_doubled(string):
    """
    Given a string, return a new string made of 2 copies of the last 4 characters of the original string.
    The string length will be at least 4.
    """
    # Your code here
    return (string[-4:] * 4)