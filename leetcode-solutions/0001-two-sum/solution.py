class Solution(object):
    def twoSum(self, nums, target):
        n=len(nums)
        hashmap={}
        for i in range(0,n):
            remaining=target-nums[i]
            if remaining in hashmap:
                return [hashmap[remaining],i]
            hashmap[nums[i]]=i

        
