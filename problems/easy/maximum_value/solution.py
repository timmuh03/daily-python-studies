"""
Docstring for problems.maximum_value.solution
The value of an alphanumeric string can be defined as:

The numeric representation of the string in base 10, if it comprises of digits only.
The length of the string, otherwise.
Given an array strs of alphanumeric strings, return the maximum value of any string in strs.
"""

class Solution:
    def maximumValue(self, strs: list[str]) -> int:
        if not strs:
            raise ValueError("Cannot accept empty list")
        
        values = []
        
        for s in strs:
            try:
                values.append(int(s))
            except ValueError:
                values.append(len(s))
        return max(values)