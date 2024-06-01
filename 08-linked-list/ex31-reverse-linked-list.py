#Given the head of a singly linked list, reverse the list, and return the reversed list.

#exercise 206

#solution without recursion

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversedList = None
        actual = head

        while actual != None:
            new_node = ListNode(actual.val, reversedList)
            reversedList = new_node
            actual = actual.next
        
        return reversedList