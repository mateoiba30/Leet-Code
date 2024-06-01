#In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.
#For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
#The twin sum is defined as the sum of a node and its twin.
#Given the head of a linked list with even length, return the maximum twin sum of the linked list.

#exercise 2130

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        reverse = None

        while fast and fast.next:#this is other way to find the middle of the list
            fast = fast.next.next #this will continue untill the end
            reverse, reverse.next, slow = slow, reverse, slow.next #on last executation, reverse will be in the middle of the list inverted

        first = reverse #first half of the original list, reversed
        second = slow #2nd half of the original list
        max_sum = -math.inf
        while first:
            if first.val + second.val > max_sum:
                max_sum = first.val + second.val
            #we are at the middle, so with first we advance untill reach its end (head of the original list) and untill the second reaches to the end
            first = first.next
            second = second.next
        return max_sum