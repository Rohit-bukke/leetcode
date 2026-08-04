class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        low=min(nums)
        high=max(nums)
        missing=[]
        for x in range(low+1,high):
            if x not in nums:
                missing.append(x)
        return missing

