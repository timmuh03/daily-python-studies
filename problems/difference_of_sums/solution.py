"""
Docstring for problems.difference_of_sums.solution
You are given positive integers n and m.

Define two integers as follows:

num1: The sum of all integers in the range [1, n] (both inclusive) that are not divisible by m.
num2: The sum of all integers in the range [1, n] (both inclusive) that are divisible by m.
Return the integer num1 - num2.
"""

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1 = 0
        num2 = 0
        
        for num in range(1, n + 1):
            if num % m != 0:
                num1 += num
            elif num % m == 0:
                num2 += num
            
        return num1 - num2
    
    # these equations will do the same thing the for loop does in O(1) time instead of O(n)
    # num2 = m * (n//m) * (n//m + 1) // 2    
    # num1 = (n * (n +1) // 2) - num2