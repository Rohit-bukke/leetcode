class Solution:
    def countCommas(self, n: int) -> int:
        # Every number from 1000 to n contains exactly 1 comma.
        if n < 1000:
            return 0
        return n - 1000 + 1

