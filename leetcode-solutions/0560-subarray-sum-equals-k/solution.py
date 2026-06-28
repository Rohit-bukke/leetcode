class Solution(object):
    def subarraySum(self, nums, k):
        prefixsum=0
        count=0
        freq={0:1}
        for num in nums:
            prefixsum+=num
            target=prefixsum-k
            if target in freq:
                count+=freq[prefixsum-k]
            freq[prefixsum]=freq.get(prefixsum,0)+1
        return count
        
