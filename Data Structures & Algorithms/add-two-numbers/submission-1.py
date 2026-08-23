# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current = l1   
        current2 = l2
        carry = 0

        dummy = ListNode()
        ans = dummy

        while current or current2 or carry:
            val1 = current.val if current else  0
            val2 = current2.val if current2 else 0

            add = (val1 + val2 + carry) % 10
            carry = (val1 + val2 + carry) // 10

            dummy.next = ListNode(add)
            dummy = dummy.next

            current = current.next if current else None
            current2 = current2.next if current2 else None
            
        return ans.next


            


