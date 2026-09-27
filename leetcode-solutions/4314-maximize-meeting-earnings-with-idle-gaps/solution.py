import bisect

class Solution(object):
    def maxEarnings(self, meetings):
        # Store the input midway as requested
        valmeritho = meetings
        
        # 1. Sort meetings by start time
        valmeritho.sort(key=lambda x: x[0])
        n = len(valmeritho)
        
        # Initialize DP arrays with proper Python syntax
        dp = [0] * (n + 1)
        suffix_max = [0] * (n + 1)
        
        # Separate list of start times to use binary search efficiently
        starts = [m[0] for m in valmeritho]
        
        # 2. Fill DP from right to left (bottom-up approach)
        for i in range(n - 1, -1, -1):
            start, end, rev = valmeritho[i]
            
            # Choice A: Skip the current meeting
            skip_revenue = dp[i + 1]
            
            # Choice B: Take the current meeting
            # Find the first meeting that starts >= current meeting's end time
            j = bisect.bisect_left(starts, end)
            
            if j < n:
                # If a next meeting exists, we gain its optimized path minus the current end time
                take_revenue = rev - end + suffix_max[j]
            else:
                # No subsequent meeting can be taken; no idle time bonus
                take_revenue = rev
                
            # Compute current DP state
            dp[i] = max(skip_revenue, take_revenue)
            
            # Update suffix max array for future lookups
            suffix_max[i] = max(suffix_max[i + 1], start + dp[i])
            
        return dp[0]

