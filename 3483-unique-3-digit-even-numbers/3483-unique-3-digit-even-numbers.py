class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        
        # Count frequency of each digit 0-9
        freq = [0] * 10
        for d in digits:
            freq[d] += 1
            
        valid_count = 0
        
        # Iterate through all 3-digit even numbers
        for num in range(100, 1000, 2):
            h = num // 100
            t = (num // 10) % 10
            u = num % 10
            
            # Count requirement for current number
            req = [0] * 10
            req[h] += 1
            req[t] += 1
            req[u] += 1
            
            # Check if we have enough of each digit
            possible = True
            for i in range(10):
                if req[i] > freq[i]:
                    possible = False
                    break
                    
            if possible:
                valid_count += 1
                
        return valid_count
