# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        h1 = list1 
        h2 = list2
        dummy = ListNode()
        c = dummy
        while(h1 and h2):
            if h1.val<=h2.val:
                temp = ListNode(h1.val)
                h1 = h1.next
            else :
                temp = ListNode(h2.val)
                h2 = h2.next
            c.next = temp
            c = c.next

        if h1:
            c.next = h1  
        elif h2:
            c.next = h2
        return dummy.next                  
                



        