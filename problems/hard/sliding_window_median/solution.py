"""
The median is the middle value in an ordered integer list. If the size of the list is even, 
there is no middle value. So the median is the mean of the two middle values.

For examples, if arr = [2,3,4], the median is 3.
For examples, if arr = [1,2,3,4], the median is (2 + 3) / 2 = 2.5.
You are given an integer array nums and an integer k. There is a sliding window of size k 
which is moving from the very left of the array to the very right. You can only see 
the k numbers in the window. Each time the sliding window moves right by one position.

Return the median array for each window in the original array. 
Answers within 10-5 of the actual value will be accepted.
 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]
Explanation: 
Window position                Median
---------------                -----
[1  3  -1] -3  5  3  6  7        1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7        3
 1  3  -1  -3 [5  3  6] 7        5
 1  3  -1  -3  5 [3  6  7]       6


 Constraints:

1 <= k <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
"""



import heapq


class Solution:
    def __init__(self):
        self.left_heap = []
        self.right_heap = []
        self.left_vcount = 0
        self.right_vcount = 0
        self.to_delete = {}
        self.result = []

    def medianSlidingWindow(self, nums: list[int], k: int) -> list[float]:
        def insert(x):
            if not self.left_heap or x <= -self.left_heap[0]:
                heapq.heappush(self.left_heap, -x)
                self.left_vcount += 1
            else:
                heapq.heappush(self.right_heap, x)
                self.right_vcount += 1

            swap()

        def balance():
            while abs(self.left_vcount - self.right_vcount) > 1:
                if self.left_vcount > self.right_vcount:
                    k = heapq.heappop(self.left_heap)
                    self.left_vcount -= 1
                    heapq.heappush(self.right_heap, -k)
                    self.right_vcount += 1
                else:
                    k = heapq.heappop(self.right_heap)
                    self.right_vcount -= 1
                    heapq.heappush(self.left_heap, -k)
                    self.left_vcount += 1

        def add_to_result():
            if k % 2 == 0:
                self.result.append((-self.left_heap[0] + self.right_heap[0]) / 2)
            else:
                if self.left_vcount >= self.right_vcount and len(self.left_heap) > 0:
                    self.result.append(-self.left_heap[0]/1)
                else:
                    self.result.append(self.right_heap[0]/1)


        def prune():
            while len(self.left_heap) > 0 and -self.left_heap[0] in self.to_delete and self.to_delete[-self.left_heap[0]] > 0:
                k = heapq.heappop(self.left_heap)
                self.to_delete[-k] -= 1
                if self.to_delete[-k] == 0:
                    del self.to_delete[-k]
            while len(self.right_heap) > 0 and self.right_heap[0] in self.to_delete and self.to_delete[self.right_heap[0]] > 0:
                k = heapq.heappop(self.right_heap)
                self.to_delete[k] -= 1
                if self.to_delete[k] == 0:
                    del self.to_delete[k]

        def swap():
            if self.left_heap and self.right_heap and -self.left_heap[0] > self.right_heap[0]:
                l = heapq.heappop(self.right_heap)
                r = -heapq.heappop(self.left_heap)
                heapq.heappush(self.left_heap, -l)
                heapq.heappush(self.right_heap, r)

            


        for num in nums[:k]:
            insert(num)
            balance()
        add_to_result()
        

        for i, num in enumerate(nums[k:]):
            outgoing = nums[i]
            if outgoing not in self.to_delete:
                self.to_delete[outgoing] = 0
            self.to_delete[outgoing] += 1
            if self.left_vcount > 0 and outgoing <= -self.left_heap[0]:
                self.left_vcount -= 1
            else:
                self.right_vcount -= 1
            prune()
            balance()
            insert(num)
            balance()
            prune()
            add_to_result()

        return self.result