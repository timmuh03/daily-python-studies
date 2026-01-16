"""
Docstring for problems.medium.binary_tree_right_side_view.solution

Given the root of a binary tree, imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.

Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Explanation:
            1 <==
          /   \\
        2        3 <==
      /   \\    /  \\
            5        4 <==

Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""
from utils.tree import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if not root: return []
        right_side = []

        def check_node(node, d):
            if not node:
                return
            if d == len(right_side):
                right_side.append(node.val)
            check_node(node.right, d + 1)
            check_node(node.left, d + 1)
       
        depth = 0
        check_node(root, depth)

        return right_side