# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        h2 = slow.next
        slow.next = None
        h1 = head

        prev = None

        while h2:
            temp = h2.next
            h2.next = prev
            prev = h2
            h2 = temp

        h2 = prev

        while h1 and h2 :
            if h1.val != h2.val:
                return False
            h1 = h1.next
            h2=h2.next
            
        return True            




        