"""
Docstring for problems.medium.course_schedule.solution

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 
1. You are given an array prerequisites where prerequisites[i] = [ai, bi] 
indicates that you must take course bi first if you want to take course ai.
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Constraints:
1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
"""


from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        next_class = [[] for _ in range(numCourses)]
        status = [0] * numCourses # 0: unvisited, 1: processing, 2: done

        for a, b in prerequisites:
            next_class[b].append(a)

        def dfs(u):
            if status[u] == 1: return True
            if status[u] == 2: return False
            status[u] = 1

            for v in next_class[u]:
                if dfs(v): return True
            
            status[u] = 2

            return False

        for i in range(len(status)):
            if status[i] == 0 and dfs(i): return False

        return True




        ### TOPO SEARCH ###
        # next_class = [[] for _ in range(numCourses)]
        # indegree = [0] * numCourses

        # for a, b in prerequisites:
        #     next_class[b].append(a)
        #     indegree[a] += 1

        # queue = deque([i for i in range(numCourses) if indegree[i] == 0])

        # taken = 0
        # while queue:
        #     c = queue.popleft()
        #     taken += 1

        #     for n in next_class[c]:
        #         indegree[n] -= 1
        #         if indegree[n] == 0:
        #             queue.append(n)

        # return taken == numCourses