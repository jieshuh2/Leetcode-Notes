# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        prev = head
        for i in range(left - 2):
            prev = prev.next
        start = prev.next if left > 1 else head
        def fixpointer(start, step):
            prev = start
            curr = start.next
            for i in range(step):
                nextnode = curr.next
                curr.next = prev
                prev = curr
                curr = nextnode
            return prev, curr
        end, follow = fixpointer(start, right - left)
        start.next = follow
        if left == 1:
            head = end
        else:
            prev.next = end
        return head