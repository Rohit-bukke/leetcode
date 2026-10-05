class Solution(object):
    def longestConsecutive(self, nums):
        my_set=set()
        for num in range(0,len(nums)):
            my_set.add(nums[num])
        longest=0
        for num in my_set:
            if num-1 not in my_set:
                x=num
                count=1
                while x+1 in my_set:
                    count+=1
                    x+=1
                longest=max(longest,count)
        return longest
        
