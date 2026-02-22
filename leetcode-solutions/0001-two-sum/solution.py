class Solution(object):
    def twoSum(self, nums, target):
       #create a hashmap and store everthing there
        arr_to_index={}
        
        for i,num in enumerate(nums):
            complement = target - num
            if complement in arr_to_index:
                return [arr_to_index[complement], i]
            arr_to_index[num] = i

        return []
        
