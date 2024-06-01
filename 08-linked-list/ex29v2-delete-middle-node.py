#You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.
#The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

#exercise 2095

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:  
        if not head.next:
            return head.next

        fast, slow = head.next.next, head #fast has a velocity of 2, slow has a velocity of 1, so when fast arrives to the end "slow" will b at the middle

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next
        #the garbage collector will delete the "actual" node
        return head