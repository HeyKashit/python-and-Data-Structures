class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        
        while fast and fast.next:
            # slow goes 1 at a time
            # fast goes 2 at a time
            # if they ever meet we know there is a cycle
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        
        return False
