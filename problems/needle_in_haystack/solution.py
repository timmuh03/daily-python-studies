'''
Docstring for needle-in-haystack
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
'''


class Solution:
    """Implements the 'needle in haystack' problem."""
    
    def strStr(self, haystack: str, needle: str) -> int:
        """Return the index of the first occurence of needle in haystack, or -1 if not found."""
        if not needle:
            return 0
        
        h, n = len(haystack), len(needle)
        for i in range(h - n + 1):
            if haystack[i:i+n] == needle:
                return i
        return -1
        
        
        """
        #one liner, but no excercise
        return 0 if needle == "" else haystack.find(needle)        
        """
        
        
        
