"""
You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. 
Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, 
but there's a constraint: there has to be a gap of at least n intervals between two tasks with the same label.

Return the minimum number of CPU intervals required to complete all tasks.


Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2

Output: 8

Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

After completing task A, you must wait two intervals before doing A again. 
The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. 
By the 4th interval, you can do A again as 2 intervals have passed.


Constraints:

1 <= tasks.length <= 104
tasks[i] is an uppercase English letter.
0 <= n <= 100
"""



class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        counts = [0] * 26
        for task in tasks:
            counts[ord(task) - ord('A')] += 1

        fmax = max(counts)
        k = counts.count(fmax) # Tail, how many elements are repeated one last time

        skele = (fmax - 1) * (n + 1) + k # (number of gaps) * (gap length + 1) + tail

        return max(skele, len(tasks)) # Can't finish in < number of tasks because tasks take one timeframe always.