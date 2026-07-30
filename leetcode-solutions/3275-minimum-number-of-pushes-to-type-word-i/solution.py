from collections import Counter

class Solution(object):
    def minimumPushes(self, word):
        # Step 1: Count frequency of each letter
        freq = Counter(word)
        
        # Step 2: Sort frequencies in descending order 
        # (most frequent letters should get fewer pushes)
        freq_list = sorted(freq.values(), reverse=True)
        
        total_pushes = 0
        keys_available = 8  # keys 2 to 9
        
        # Step 3: Distribute letters across 8 keys
        # First 8 letters get 1 push each, next 8 get 2 pushes each, etc.
        for i, f in enumerate(freq_list):
            push_count = (i // keys_available) + 1
            total_pushes += push_count * f
        
        return total_pushes
