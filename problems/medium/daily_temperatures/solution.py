"""
Docstring for problems.medium.daily_temperatures.solution
Given an array of integers temperatures represents the daily temperatures, 
return an array answer such that answer[i] is the number of days you have to wait 
after the ith day to get a warmer temperature. If there is no future day for which 
this is possible, keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Constraints:
1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
"""


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        unresolved = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):

            while unresolved and temperatures[i] > temperatures[unresolved[-1]]:
                index = unresolved.pop()
                result[index] = i - index
               
            unresolved.append(i)

        return result