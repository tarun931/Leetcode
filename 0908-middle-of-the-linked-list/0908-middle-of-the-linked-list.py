# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        cur = head
        fast = head.next
        while(fast.next and fast.next.next):
            cur = cur.next
            fast = fast.next.next
        cur = cur.next
        return cur    

             
               
        