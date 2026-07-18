class Solution(object):
    def findGCD(self, nums):
        smallest=min(nums)
        largest=max(nums)
        # for i in range(len(nums)):
        #     if(nums[i]<smallest):
        #         smallest=nums[i]
        #     if(nums[i]>largest):
        #         largest=nums[i]
        
    
        while smallest:
            largest,smallest=smallest,largest%smallest
        return largest
        
