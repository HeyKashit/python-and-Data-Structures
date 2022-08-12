class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode()
        current = dummyNode
        pointer1 = list1
        pointer2 = list2
        
        while pointer1 and pointer2:
            if pointer1.val < pointer2.val:
                current.next = pointer1
                pointer1 = pointer1.next
            else:
                current.next = pointer2
                pointer2 = pointer2.next
            current = current.next
        
        if pointer1:
            current.next = pointer1
        if pointer2:
            current.next = pointer2
        
        return dummyNode.next
