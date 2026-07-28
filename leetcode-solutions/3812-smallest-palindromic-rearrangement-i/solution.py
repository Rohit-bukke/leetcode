class Solution(object):
    def smallestPalindrome(self, s):
        # 1. Fast frequency count using a fixed array of size 26
        counts = [0] * 26
        for char in s:
            counts[ord(char) - 97] += 1
        
        left_half = []
        mid_char = ""
        
        # 2. Build the halves using list appends (O(1) time)
        for i in range(26):
            freq = counts[i]
            if freq > 0:
                char = chr(i + 97)
                if freq % 2 == 1:
                    mid_char = char
                left_half.append(char * (freq // 2))
                
        # 3. Join everything once at the end
        left_str = "".join(left_half)
        return left_str + mid_char + left_str[::-1]

