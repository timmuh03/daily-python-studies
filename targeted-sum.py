'''
Targeted Sum
Given an array of numbers and an integer target, find two unique numbers in the array that add up to the target value. 
Return an array with the indices of those two numbers, or "Target not found" if no two numbers sum up to the target.

The returned array should have the indices in ascending order.
'''

def find_target(arr, target):
    '''
    Return indicies of two numbers that add up to target.
    Assumes exactly one solution exists and same element can't be used more than once.
    '''
    if len(arr) < 2:
        return None
    
    values = {}
    
    for i in range(len(arr)):
        if -arr[i] + target in values: # Compliment of numbers already seen
            return [values[-arr[i] + target], i]
        values[arr[i]] = i  # Map current_value:index

    return "Target not found"




print(find_target([2, 7, 11, 15], 9))          # Expected: [0, 1]
print(find_target([1, 2, 3, 4], 100))          # Expected: "Target not found"
print(find_target([-3, 4, 1, 2], -1))          # Expected: [0, 3]
print(find_target([0, 4, 3, 0], 0))            # Expected: [0, 3]
print(find_target([1, 5, 5, 3], 10))           # Expected: [1, 2]
print(find_target([7], 7))                     # Expected: "None"
print(find_target([], 10))                     # Expected: "None"
print(find_target([10**9, 3, -10**9], 3))      # Expected: "Target not found"
print(find_target([8, 1, 2, 9, 5, 4], 9))      # Expected: [0, 1]  
print(find_target([3, 3, 3], 6))               # Expected: [0, 1]
print(find_target([-10, 20, 5, -5], 10))       # Expected: [0, 1]
print(find_target([1.5, 2.5, 3.0], 4.0))       # Expected: [0, 1]

