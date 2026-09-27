from collections import Counter

class Solution(object):
    def rearrangeArray(self, nums):
        # 1. Count the frequency of each number
        counts = Counter(nums)
        ans = []
        
        # 2. Keep looping until all frequencies drop to 0
        while counts:
            # Identify all distinct values currently present
            distinct_elements = list(counts.keys())
            
            # Sort them in ascending order as requested
            distinct_elements.sort()
            
            # Append them to our answer array
            ans.extend(distinct_elements)
            
            # Remove one occurrence of every distinct value
            for num in distinct_elements:
                counts[num] -= 1
                # If a number's count hits 0, remove it from the pool
                if counts[num] == 0:
                    del counts[num]
                    
        return ans

