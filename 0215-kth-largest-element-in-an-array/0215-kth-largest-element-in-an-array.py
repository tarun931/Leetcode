class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = [-num for num in nums]
        heapq.heapify(n)
        for i in range(0,k-1):
            heapq.heappop(n)
        return -1*heapq.heappop(n)      
            



        


# def findKthLargest(self, nums: List[int], k: int) -> int:
#         heap = nums[:k]
#         heapq.heapify(heap)
        
#         for num in nums[k:]:
#             if num > heap[0]:
#                 heapq.heappop(heap)
#                 heapq.heappush(heap, num)
        
#         return heap[0]



        