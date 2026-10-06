class Solution(object):
    def minAddToMakeValid(self, s):
        # Tracks how many '(' are currently "open" and waiting for a ')'
        open_needed = 0
        
        # Tracks how many times a ')' appeared with no matching '(' before it
        insertions = 0
        
        for char in s:
            if char == '(':
                # We found an opening bracket; it is waiting for a ')'
                open_needed += 1
            else:  # char == ')'
                if open_needed > 0:
                    # We have a waiting '('. This ')' pairs up with it!
                    # One '(' is now satisfied, so decrement.
                    open_needed -= 1
                else:
                    # No '(' is waiting. This ')' has nobody to match with.
                    # The only way to fix it is to insert a '(' right in front of it.
                    insertions += 1
                    
        # Final answer:
        # - 'insertions' = all the '(' we needed to add to fix stray ')'
        # - 'open_needed' = all the stray '(' left over that need a ')' added at the end
        return insertions + open_needed
