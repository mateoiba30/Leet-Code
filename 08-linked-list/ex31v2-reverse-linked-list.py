#Given the head of a singly linked list, reverse the list, and return the reversed list.

#exercise 206

#this solution is with recursion

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(not head or not head.next): #base case
            return head
        
        aux = head.next
        new_head = self.reverseList(head.next) #we need to reverse all the other nodes
        aux.next = head #once all nodes are reversed, we only need to put the 2nd node aux at the start
        head.next = None #if we dont do this, the list will be a circle
        
        return new_head