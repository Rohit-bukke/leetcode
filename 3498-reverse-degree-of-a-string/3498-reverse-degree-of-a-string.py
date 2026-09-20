class Solution(object):
    def reverseDegree(self, s):
        total_sum = 0
        string_index = 1  # Manual counter for 1-based indexing
        
        for char in s:
            # Calculate position in the reversed alphabet ('a'=26, 'b'=25, ..., 'z'=1)
            rev_alphabet_index = 26 - (ord(char) - ord('a'))
            
            # Multiply by the string index and add to the total sum
            total_sum += rev_alphabet_index * string_index
            
            # Increment the index for the next character
            string_index += 1
            
        return total_sum
