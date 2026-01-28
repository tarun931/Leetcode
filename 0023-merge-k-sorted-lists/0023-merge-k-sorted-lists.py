# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


#mergesort -> divide the lists into two sections. , call merge on each section
#merge -> merge the two linked list you recieve 

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:    
        if not lists or len(lists)==0:
                return None
        while(len(lists)>1):
            merged = []
            for i in range(0,len(lists),2):
                list1 = lists[i]
                list2 = lists[i+1] if (i+1)<len(lists) else None
                merged.append(self.mergesort(list1 , list2))
            lists = merged
        return lists[0]                

    def mergesort(self, l1 , l2):
        dummy = ListNode()
        h1 = l1 
        h2 = l2
        c = dummy
        while(h1 and h2):
            if h1.val<= h2.val:
                c.next = h1
                h1 = h1.next
            else:
                c.next = h2
                h2 = h2.next
            c= c.next
        if h1:
            c.next = h1
        if h2:
            c.next = h2
        return dummy.next            





        