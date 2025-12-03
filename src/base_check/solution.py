'''
Given a string representing a number, and an integer base from 2 to 36, determine whether the number is valid in that base.

The string may contain integers, and uppercase or lowercase characters.
The check should be case-insensitive.
The base can be any number 2-36.
A number is valid if every character is a valid digit in the given base.
Example of valid digits for bases:
Base 2: 0-1
Base 8: 0-7
Base 10: 0-9
Base 16: 0-9 and A-F
Base 36: 0-9 and A-Z
'''

class Solution:
    def is_valid_number(self, n, base):
        '''
        Checks if a string is valid for a given base
        '''
        
        # Requires something in n
        if not n or base > 36:
            return False
        
        lower_n = n.lower()                                 # Case insensitive
        range_map = '0123456789abcdefghijklmnopqrstuvwxyz'  # Allowed characters up to base 36
            
        for char in lower_n:
            if char not in range_map[:base]:                # Only check up to base
                return False        

        return True


