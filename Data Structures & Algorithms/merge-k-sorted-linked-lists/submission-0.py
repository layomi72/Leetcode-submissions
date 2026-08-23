# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                l1 = i
                l2 = i + 1 if i + 1 < len(lists) else None
                z = lists[l2] if l2 != None else None

                sort = self.merge(lists[l1],z)
                merged.append(sort)

            lists = merged

        
        return lists[0]












    def merge(self, x:[Optional[ListNode]], y:[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
       
       
        current = dummy
        while x and y:
            if x.val <= y.val:
                current.next = x
                x = x.next

            else:
                current.next = y
                y = y.next
            
            current = current.next
          

        while y:
            current.next = y
            current = current.next
            y = y.next

        while x:
            current.next = x
            current = current.next
            x = x.next

        return dummy.next
            
