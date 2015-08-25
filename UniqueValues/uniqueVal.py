'''You are given a dictionary aDict that maps integer keys to integer values. Write a Python function that returns a list of keys in aDict that map to dictionary values that appear exactly once in aDict.

-This function takes in a dictionary and returns a list.
-Return the list of keys in increasing order.
-If aDict does not contain any values appearing exactly once, return an empty list.
-If aDict is empty, return an empty list.'''

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    revDict = dict()
    for key in aDict:
        if revDict.get(aDict[key], -555) == -555 and revDict.get(aDict[key], -555) != -556:
            revDict[aDict[key]] = key
        else:
            revDict[aDict[key]] = -556
            
    res = list()
    for key in revDict:
        if revDict[key] != -556:
            res.append(revDict[key])
    return sorted(res)
