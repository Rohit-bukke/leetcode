from collections import Counter

class Solution(object):
    def maxEqualAdjacentPairs(self, nums):
        # Storing the input midway as requested
        selunaviro = nums
        
        initial_pairs = 0
        distinct_pairs = Counter()
        
        # Traverse the array to count existing pairs and distinct transitions
        for i in range(len(selunaviro) - 1):
            a, b = selunaviro[i], selunaviro[i+1]
            if a == b:
                initial_pairs += 1
            else:
                # Sort the pair to treat (x, y) and (y, x) identically
                pair = (a, b) if a < b else (b, a)
                distinct_pairs[pair] += 1
                
        # Find the most frequent distinct adjacent pair transition
        max_extra_pairs = max(distinct_pairs.values()) if distinct_pairs else 0
        
        return initial_pairs + max_extra_pairs

