"""
Given a linked list, swap every two adjacent nodes and return its head. 
You must solve the problem without modifying the values in the list's nodes 
(i.e., only nodes themselves may be changed.)


Example 1:

Input: head = [1,2,3,4]

Output: [2,1,4,3]

Explanation:
1 -> 2 -> 3 -> 4
2 -> 1 -> 4 -> 3


Constraints:

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100
"""


from src.utils.list_single import ListNode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        while prev.next and prev.next.next:
            a = prev.next
            b = prev.next.next
            next_pair = prev.next.next.next

            prev.next = b
            b.next = a
            a.next = next_pair

            prev = a

        return dummy.next