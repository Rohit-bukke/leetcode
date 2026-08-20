class Solution(object):
    def resultArray(self, nums):
        # First operation: append nums[0] to arr1
        arr1 = [nums[0]]
        # Second operation: append nums[1] to arr2
        arr2 = [nums[1]]
        
        # Process the remaining elements
        for i in range(2, len(nums)):
            # Compare the last elements of both arrays
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
                
        # Return the concatenated result
        return arr1 + arr2

