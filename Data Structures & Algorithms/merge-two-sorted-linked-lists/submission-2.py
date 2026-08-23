# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list11 = []
        sorted_list = []
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        head1 = list1
        while (head1 != None):
            list11.append(head1.val)
            head1 = head1.next
        
        head2 = list2
        while (head2 != None):
            list11.append(head2.val)
            head2 = head2.next
        
        sorted_list = sorted(list11)
        sorted_link = ListNode(sorted_list[0])
        head3 = sorted_link

        for i in range(1,len(sorted_list)):
            head3.next = ListNode(sorted_list[i])
            head3 = head3.next
        
        
        return sorted_link
        
