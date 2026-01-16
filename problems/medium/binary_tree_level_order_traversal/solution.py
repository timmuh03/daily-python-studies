"""
Docstring for problems.medium.binary_tree_level_order_traversal.solution

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

                    3
                  /   \\
                9       20
                      /   \\
                     15     7

Constraints:
The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from src.utils.tree import TreeNode



class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root: return []
        result = []

        nodes = deque([root])
        while nodes:
            level_vals = []
            for _ in range(len(nodes)):
                node = nodes.popleft()

                level_vals.append(node.val)
                if node.left is not None:
                    nodes.append(node.left)
                if node.right is not None:
                    nodes.append(node.right)
            result.append(level_vals)
            
        return result