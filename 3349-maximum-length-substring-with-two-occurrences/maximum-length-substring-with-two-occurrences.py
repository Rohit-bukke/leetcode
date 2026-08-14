from collections import defaultdict

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        max_len = 0
        left_ptr = 0
        char_counts = defaultdict(int)
        
        # Expand the sliding window using the right pointer
        for right_ptr in range(len(s)):
            char_counts[s[right_ptr]] += 1
            
            # Shrink the window from the left until the count of s[right_ptr] is at most 2
            while char_counts[s[right_ptr]] > 2:
                char_counts[s[left_ptr]] -= 1
                left_ptr += 1
                
            # Keep track of the maximum window size seen so far
            max_len = max(max_len, right_ptr - left_ptr + 1)
            
        return max_len
