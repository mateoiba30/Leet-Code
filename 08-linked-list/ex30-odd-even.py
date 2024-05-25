#Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.
#The first node is considered odd, and the second node is even, and so on.
#Note that the relative order inside both the even and odd groups should remain as it was in the input.
#You must solve the problem in O(1) extra space complexity and O(n) time complexity."

#excercise 328

from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        odd = head #the first is odd, and the odd_head is head
        even_head = head.next #the second is even
        even = even_head 
        while even and even.next: #while we have 2 values (and odd and an even)
            odd.next = even.next #next to the even is gonna be the following od

            odd = odd.next #advance
            
            even.next = odd.next #we do the same for the even
            even = even.next

        odd.next = even_head#with the previous loop we end analizing an even, but we finally need to connect
        return head #return the odd_head
    
nodo5 = ListNode(5)
nodo4 = ListNode(4, nodo5)
nodo3 = ListNode(3, nodo4)
nodo2 = ListNode(2, nodo3)
nodo1 = ListNode(1, nodo2)

sol = Solution()
nuevo_head = sol.oddEvenList(nodo1)
while nuevo_head != None:
    print(nuevo_head.val)
    nuevo_head = nuevo_head.next
