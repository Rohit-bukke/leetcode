import collections

class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        # Map each row to a set of reserved seat numbers
        row_map = collections.defaultdict(set)
        for row, seat in reservedSeats:
            row_map[row].add(seat)
        
        # Unreserved rows can accommodate 2 families each
        count = (n - len(row_map)) * 2
        
        # Check each row with at least one reservation
        for row, seats in row_map.items():
            left = not (2 in seats or 3 in seats or 4 in seats or 5 in seats)
            right = not (6 in seats or 7 in seats or 8 in seats or 9 in seats)
            middle = not (4 in seats or 5 in seats or 6 in seats or 7 in seats)
            
            if left and right:
                count += 2
            elif left or right or middle:
                count += 1
                
        return count

