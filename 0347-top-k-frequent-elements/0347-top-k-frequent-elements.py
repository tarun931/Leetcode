class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d ={}
        for i in range(0, len(nums)):
            if nums[i] not in d :
                d[nums[i]] = 1
            else :
                d[nums[i]] += 1        
        
        maxHeap = [(-freq , ele) for ele , freq in d.items()]
        # for key, val in counter.items():
        #     heapq.heappush(heap, (-val, key))

        heapq.heapify(maxHeap)

        ans = []

        for i in range(k , 0 ,-1):
            _ , ele = heapq.heappop(maxHeap)
            print(ele)
            ans.append(ele)    
        return ans    



        