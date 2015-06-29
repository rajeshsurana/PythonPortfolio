def longest_alphabetical_seq(s):
    """s:String
       returns longest alphabetical sequence"""
    low = 0
    res = ''
    length = len(s)
    iterator = 0
    while iterator + 1 < length:
        if s[iterator] > s[iterator + 1]:
            if len(s[low:iterator+1]) > len(res):
                res = s[low:iterator+1]
            low = iterator + 1
        iterator += 1
    if iterator + 1 == length:
        if len(s[low:iterator+1]) > len(res):
            res = s[low:iterator+1]
    
    return res

print "Longest Alphabetical Sequence: "+longest_alphabetical_seq(raw_input('Input String to find longest alphabetical sequence:'))
