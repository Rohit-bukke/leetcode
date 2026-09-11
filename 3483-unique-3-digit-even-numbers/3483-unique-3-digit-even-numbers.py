class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        unique_numbers = set()
        n = len(digits)
        # Try all unique positions for the three digits
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    # Ensure we don't reuse the exact same array position
                    if i != j and j != k and i != k:
                        # No leading zeros
                        if digits[i] != 0: 
                            # Must be an even number
                            if digits[k] % 2 == 0: 
                                # Form the 3-digit number
                                num = digits[i] * 100 + digits[j] * 10 + digits[k]
                                unique_numbers.add(num)
                                
        return len(unique_numbers)