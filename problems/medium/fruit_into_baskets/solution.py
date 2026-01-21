"""
Docstring for problems.medium.fruit_into_baskets.solution

You are visiting a farm that has a single row of fruit trees arranged from left to right. 
The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.
You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:
You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree 
(including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.

Example 1:
Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.

Constraints:
1 <= fruits.length <= 105
0 <= fruits[i] < fruits.length
"""



from collections import defaultdict


class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        left = 0
        counts = defaultdict(int)
        result = 0

        for i, fruit in enumerate(fruits):
            counts[fruit] += 1
                
            while len(counts) > 2: # Loop while window is invalid
                l_fruit = fruits[left]
                counts[l_fruit] -= 1
                if counts[l_fruit] == 0:
                    del counts[l_fruit] # Remove 0 count fruits to keep validity check correct
                left += 1

            length = i - left + 1
            if length > result: result = length # Window is always valid here so it's a possible best length


        return result