"""
Docstring for can_be_equal.solution
You are given two integer arrays of equal length target and arr. 
In one step, you can select any non-empty subarray of arr and reverse it. 
You are allowed to make any number of steps.

Return true if you can make arr equal to target or false otherwise.
"""


from collections import Counter

class Solution:
    def canBeEqual(self, target: list[int], arr: list[int]) -> bool:
        return Counter(arr) == Counter(target)
        
        #THE BELOW CODE IS BECAUSE I WANTED TO REMEMBER HOW TO REVERSE SUBSTRINGS
        # fun_target = target
        # fun_arr = arr        
        # count = 0
        
        # print('*' * 10, 'start', '*' * 10)
    
        # while fun_target != fun_arr and count < len(arr):
        #     print('count', count)
        #     if fun_arr[count] not in fun_target:
        #         return False
            
        #     for i in range(count, len(fun_arr)):
        #         print(fun_arr, fun_target)
        #         if fun_arr[i] == fun_target[count]:
        #             print(fun_arr[i], fun_target[count], "<----Match")
        #             print(count, i)
        #             reverse fun_arr[count:i]
        #             for pointer in range(len(fun_arr[count:i])):
        #                 print('reversing')
        #                 fun_arr[count + pointer], fun_arr[i - pointer] = fun_arr[i - pointer], fun_arr[count + pointer]                 
                    
        #     count += 1
        # return arr == target