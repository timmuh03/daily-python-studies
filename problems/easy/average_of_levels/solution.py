from src.utils.tree import TreeNode
from collections import deque


"""
Docstring for tests.test_average_of_levels
Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. 
Answers within 10^-5 of the actual answer will be accepted.
"""
        
class Solution:
    def averageOfLevels(self, root: TreeNode | None) -> list[float]:
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            level_sum = 0
            
            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val or 0
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            result.append(level_sum / level_size)
        
        return result
    