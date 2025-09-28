# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next :
            return head

        prev = None
        cur = head
        forw = head.next

        while(forw):
            cur.next = prev 
            prev = cur
            cur = forw
            forw = forw.next
        
        cur.next = prev
        return cur    


        