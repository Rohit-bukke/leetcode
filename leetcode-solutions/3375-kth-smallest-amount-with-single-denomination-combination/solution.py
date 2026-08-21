import math

class Solution(object):
    def findKthSmallest(self, coins, k):
        # Helper to compute Greatest Common Divisor
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        # Helper to compute Least Common Multiple
        def lcm(a, b):
            return (a * b) // gcd(a, b)

        n = len(coins)
        # Precompute LCMs for all possible combinations of coins
        # We store (lcm_value, sign) where sign is +1 for odd count, -1 for even count
        subsets = []
        for i in range(1, 1 << n):
            current_lcm = 1
            count = 0
            for j in range(n):
                if (i >> j) & 1:
                    current_lcm = lcm(current_lcm, coins[j])
                    count += 1
            
            # If count is odd, we add the multiples (+1)
            # If count is even, we subtract the duplicates (-1)
            sign = 1 if count % 2 == 1 else -1
            subsets.append((current_lcm, sign))

        # Helper function to count total multiples <= mid using PIE
        def count_multiples(mid):
            total = 0
            for lcm_val, sign in subsets:
                total += sign * (mid // lcm_val)
            return total

        # Binary search for the kth smallest amount
        # Lower bound is the minimum coin, upper bound is the worst-case scenario
        low = min(coins)
        high = min(coins) * k
        ans = high

        while low <= high:
            mid = (low + high) // 2
            if count_multiples(mid) >= k:
                ans = mid
                high = mid - 1  # Try to find a smaller valid amount
            else:
                low = mid + 1   # Increase the range

        return ans

        
        
