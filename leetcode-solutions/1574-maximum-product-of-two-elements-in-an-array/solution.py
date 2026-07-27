class Solution(object):
    def maxProduct(self, nums):
        # Initialize the two largest values to negative infinity
        largest = float('-inf')
        second_largest = float('-inf')
        # Single pass to find the top two maximum values
        for num in nums:
            if num > largest:
                second_largest = largest
                largest = num
            elif num > second_largest:
                second_largest = num
                
        return (largest - 1) * (second_largest - 1)

