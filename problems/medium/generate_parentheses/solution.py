"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
"""



class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        opens = 0
        unclosed = 0
        partial = ""
        def dfs(partial, opens, unclosed):
            if len(partial) == 2*n: res.append(partial); return

            if opens < n:
                dfs(partial + "(", opens + 1, unclosed + 1)

            if unclosed > 0:
                dfs(partial + ")", opens, unclosed - 1)

        dfs(partial, opens, unclosed)

        return res