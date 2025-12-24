"""
Docstring for problems.medium.top_K_frequent.solution
Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Constraints:
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
"""
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counted_nums = Counter(nums)
        
        # using heap
        heap = []
        for key, val in counted_nums.items():
            if len(heap) < k:
                heapq.heappush(heap, (val, key))
            elif heap[0][0] < val:
                heapq.heapreplace(heap, (val, key))
        print(heap)
        return [x for _, x in heap]
        
        # using buckets
        # buckets = [[] for _ in range(len(nums) + 1)]
        # for key, val in counted_nums.items():
        #     buckets[val].append(key)
        # result = []
        # freq = len(buckets) - 1
        # while len(result) < k and freq > 0:
        #     for x in buckets[freq]:
        #         result.append(x)
        #     freq -= 1
        # return result[:k]
    
        # using sorted
        # sorted_nums = sorted(counted_nums.items(), key=lambda item: item[1], reverse=True)
        # return [num for num, _ in sorted_nums[:k]]