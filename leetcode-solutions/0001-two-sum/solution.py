class Solution(object):
    def twoSum(self, nums, target):
        mpp={}
        for i in range(0,len(nums)):
            a=nums[i]
            more=target-a
            if(more in mpp):
                return [mpp[more],i]
            mpp[a]=i
        return "no"
        
