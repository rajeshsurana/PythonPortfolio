'''
Write a Python function called satisfiesF that has the specification below. Then make the function call run_satisfiesF(L, satisfiesF).
'''
def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements
    Returns the length of L after mutation
    """
    res = []
    for s in L:
        if f(s):
            res.append(s)
    L[:] = res
    return len(L)

#run_satisfiesF(L, satisfiesF)
def f(s):
    return 'a' in s
L =  ['a', 'b', 'a']   
print satisfiesF(L)
print L