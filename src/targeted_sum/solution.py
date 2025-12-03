'''
Targeted Sum
Given an array of numbers and an integer target, find two unique numbers in the array that add up to the target value. 
Return an array with the indices of those two numbers, or "Target not found" if no two numbers sum up to the target.

The returned array should have the indices in ascending order.
'''
class Solution:
    def find_target(self, arr, target):
        '''
        Return indicies of two numbers that add up to target.
        Assumes exactly one solution exists and same element can't be used more than once.
        '''
        if len(arr) < 2:
            return "Array length error"
        
        values = {}
        
        for i in range(len(arr)):
            if -arr[i] + target in values: # Compliment of numbers already seen
                return [values[-arr[i] + target], i]
            values[arr[i]] = i  # Map current_value:index

        return "Target not found"



