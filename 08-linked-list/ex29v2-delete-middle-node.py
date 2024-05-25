from typing import Optional
from typing import ListNode

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