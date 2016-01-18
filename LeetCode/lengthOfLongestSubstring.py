"""
Given a string, find the length of the longest substring without repeating characters. For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        myset = set()
        result = 0
        start = 0
        length = len(s)
        i = 0
        while(i<length):
            current = s[i]
            if(current in myset):
                result = max(result, i-start)
                for k in range(start, i):
                    if s[k] == current:
                        start = k + 1
                        break
                    myset.discard(s[k])
            else:
                myset.add(s[i])
            i+=1
        return max(result, length - start)