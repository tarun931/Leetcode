# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(nums , i , j):
            if i>j:
                return None
            if i==j:
                return TreeNode(nums[i])
            mid = (j+i)//2 
            node = TreeNode(nums[mid])
            node.left = helper(nums,i,mid-1 )
            node.right = helper(nums, mid+1 , j)
            return node
        return helper(nums , 0 , len(nums)-1)           
        