# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     if not head or not head.next:
    #         return head
    #     dummy = self.reverseList(head.next)
    #     head.next.next = head
    #     head.next = None
    #     return dummy
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        cur = head
        dummy = None
        forw = head.next    
        while(cur.next):
            cur.next = dummy
            dummy = cur
            cur = forw
            forw = cur.next
        cur.next = dummy
        return cur        
        


           
        