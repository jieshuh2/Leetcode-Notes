#brute force solution will be merge 1 list a time or even slower loop through all the list to find the minimum, the timecomplexity will be kn
#but base on the idea of mergesort. We merge 2 list on time so the total time complexity is log(k)*n
import math
class Solution:
    def merge2Lists(self, list1, list2):
        head = ListNode()
        node = head
        while list1 and list2:
            if list1.val <= list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        if list1:
            node.next = list1
        if list2:
            node.next = list2
        return head.next
                
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        while len(lists) > 1:
            newlists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                reslist = self.merge2Lists(l1,l2)
                newlists.append(reslist)
            lists = newlists
        return lists[0]