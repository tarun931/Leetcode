class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        vals = [[i,nums[i]] for i in range(0,n)]
        vals.sort(key = lambda x:-x[1])
        vals = sorted(vals[: k])
        vals = [ val for i,val in vals ]
        return vals
        



#         \U0001f528 How to Write Them Yourself (Step-by-Step)


# Start with a for-loop:
# for item in something:
#     ...


# Decide what you want to collect:
# result = [item for item in something]


# Add a condition (optional):
# result = [item for item in something if condition]

# Transform while collecting (optional):
# result = [transform(item) for item in something if condition]