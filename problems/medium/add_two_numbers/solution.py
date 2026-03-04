"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.


Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.


Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""


from src.utils.list_single import ListNode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        result_head = ListNode() # Need a sentinel to keep track of the head
        result_head.next = ListNode()
        result = result_head.next
        carry = 0

        while l1 or l2 or carry: # True if there's a value for another digit
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            s = val1 + val2 + carry
            result.val = s % 10
            carry = s // 10 # carry for next digit

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
            if l1 or l2 or carry:
                result.next = ListNode()
                result = result.next

        return result_head.next
        