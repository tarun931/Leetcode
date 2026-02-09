class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ind = {}
        ans = []
        for i in range(0, len(nums2)):
            ind[nums2[i]] = i

        for i in range(0, len(nums1)):
            index = ind[nums1[i]]
            ele = nums1[i]
            flag = 0
            for j in range(index+1 ,len(nums2)):
                if nums2[j] > ele:
                    ans.append(nums2[j])
                    flag = 1
                    break
            if flag == 0:
                ans.append(-1)        


        return ans            

        