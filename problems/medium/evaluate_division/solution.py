"""
Docstring for problems.medium.evaluate_division.solution

You are given an array of variable pairs equations and an array of real numbers values, 
where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. 
Each Ai or Bi is a string that represents a single variable.
You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query 
where you must find the answer for Cj / Dj = ?.
Return the answers to all queries. If a single answer cannot be determined, return -1.0.
Note: The input is always valid. You may assume that evaluating the queries will not result 
in division by zero and that there is no contradiction.
Note: The variables that do not occur in the list of equations are undefined, 
so the answer cannot be determined for them.

Example 1:
Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
note: x is undefined => -1.0

Constraints:
1 <= equations.length <= 20
equations[i].length == 2
1 <= Ai.length, Bi.length <= 5
values.length == equations.length
0.0 < values[i] <= 20.0
1 <= queries.length <= 20
queries[i].length == 2
1 <= Cj.length, Dj.length <= 5
Ai, Bi, Cj, Dj consist of lower case English letters and digits.
"""



class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        # parent[x] is x's representative link; following parent laeds to the component "root".
        parent = {}

        # Invariant: x = weight[x] * parent[x] | weight[x] is the conversion factor from parent[x] to x.
        weight = {}
        result = []

        def initialize(n):
            # Every variable gets identity mapping before linking. (x = 1.0 * x) Starts as its own component.
            if n not in parent:
                parent[n] = n
                weight[n] = 1.0

        def find(x):
            # Returns (root, ratio) such that x = ratio * root. Path compression present to save on work.
            if parent[x] == x:
                return (x, 1.0)
            
            p = parent[x]
            root, ratioP = find(p)

            # If x = weight[x] * p and p = ratioP * root, then x = (weight[x] * ratioP) * root.
            ratioX = weight[x] * ratioP

            # Compress path: point x directly to root
            parent[x] = root
            weight[x] = ratioX

            return (root, ratioX)

        # Precompute connectivity + ratios by merging components using each equation a / b = k.
        for (a, b), k in zip(equations, values):
            initialize(a)
            initialize(b)
        
            rootA, ratioA = find(a)
            rootB, ratioB = find(b)

            if rootA != rootB:
                # Attach rootA under rootB and with the scaling factor that keeps a / b = k true.
                parent[rootA] = rootB
                weight[rootA] = (k * ratioB) / ratioA

        # Answer queries using the precomputed component structure.
        for x, y in queries:
            # Variables not present in any equation are undefined.
            if x in parent and y in parent:
                rootX, ratioX = find(x) # x = ratioX * rootX
                rootY, ratioY = find(y) # y = ratioY * rootY
                if rootX != rootY:
                    # Different roots don't have connecting equation chains so no ratio can be determined.
                    r = -1.0
                else:
                    # Same root means x/root and y/root are comparable
                    r = ratioX / ratioY
            else:
                r = -1.0
            result.append(r)

        return result

        
            