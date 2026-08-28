# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        curr = head
        hash_set = set()
        while curr is not None:
            if curr in hash_set:
                return True
            hash_set.add(curr)
            curr = curr.next
        return False