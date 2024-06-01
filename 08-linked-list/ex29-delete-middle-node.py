#You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.
#The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

#exercise 2095

from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        actual = head
        cont = 0

        while actual != None:
            cont +=1
            actual = actual.next

        middle_pos = cont // 2

        if cont <= 1:
            return None
        
        cont = 0
        actual = head
        prev = head
        while cont != middle_pos:
            cont+=1
            prev = actual 
            actual = actual.next

        prev.next = actual.next
        #the garbage collector will delete the "actual" node
        return head


