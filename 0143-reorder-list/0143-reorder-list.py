# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        h1 = head
        slow = head
        fast = head.next
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        h2 = slow.next
        slow.next = None
        # h1 and h2 are two list now 

        #reverse h2

        prev = None
        while h2:
            tmp = h2.next
            h2.next = prev
            prev = h2
            h2= tmp
        h2 = prev
        #merge h1 and reversed h2
        
        # head1 = h1
        while(h1 and h2):
            tmp1 , temp2 = h1.next , h2.next
            h1.next = h2
            h2.next = tmp1
            h1  , h2 = tmp1 , temp2



        