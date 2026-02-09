"""
Docstring for problems.medium.redundant_connection.solution

In this problem, a tree is an undirected graph that is connected and has no cycles.
You are given a graph that started as a tree with n nodes labeled from 1 to n, 
with one additional edge added. The added edge has two different vertices chosen from 1 to n, 
and was not an edge that already existed. The graph is represented as an array edges of length n 
where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.
Return an edge that can be removed so that the resulting graph is a tree of n nodes. 
If there are multiple answers, return the answer that occurs last in the input.

Example 1:
Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]

Constraints:
n == edges.length
3 <= n <= 1000
edges[i].length == 2
1 <= ai < bi <= edges.length
ai != bi
There are no repeated edges.
The given graph is connected.
"""



class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        n = len(edges) + 1
        parent = [i for i in range(n)] # Every node starts as its own progenitor (singleton components)
        size = [1] * n # Track component sizes for union decisions.

        def find(x):
            # Returns progenitor of x and compresses the path.
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]
            
        for x, y in edges:
            px = find(x)
            py = find(y)

            if px == py: # Indicates redundant connection
                return [x, y]
            else:
                # Keep tree height as small as possible
                if size[px] < size[py]:
                    px, py = py, px
                parent[py] = px
                size[px] += size[py]
                
        return []