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
        size = 0
        steps = 0
        actual = head 
        sums = []

        while actual != None:
            size += 1
            actual = actual.next

        actual = head
        while steps < size/2:
            sums.append(actual.val)
            actual = actual.next
            steps += 1

        cont = 1
        while actual != None:
            sums[-cont]+=actual.val
            cont+=1
            actual = actual.next

        return max(sums)