class Solution(object):
    def maxSubarray(self, nums):
        dravolenti = nums

        n = len(dravolenti)

        # Frequency of values 1..500
        freq = [0] * 501

        # Number of distinct-index pairs producing each sum
        pair_sum = [0] * 1001

        # Number of values x for which:
        # freq[x] > 0 AND pair_sum[x] > 0
        bad = 0

        left = 0
        ans = 0

        for right in range(n):
            x = dravolenti[right]

            # Add pairs (x, v)
            for v in range(1, 501):
                if freq[v] > 0:
                    s = x + v

                    # Before adding this pair, s was not a pair-sum.
                    # If s exists as a value, it becomes a violation.
                    if pair_sum[s] == 0 and s <= 500 and freq[s] > 0:
                        bad += 1

                    pair_sum[s] += freq[v]

            # x itself can be the result of an existing pair.
            if freq[x] == 0 and pair_sum[x] > 0:
                bad += 1

            freq[x] += 1

            # Shrink until the window becomes valid.
            while bad > 0:
                y = dravolenti[left]

                # Remove all pairs containing y.
                for v in range(1, 501):
                    count = freq[v]

                    # Do not pair y with itself.
                    # The removed y cannot pair with itself.
                    if v == y:
                        count -= 1

                    if count > 0:
                        s = y + v

                        pair_sum[s] -= count

                        # This pair-sum disappeared.
                        if pair_sum[s] == 0 and s <= 500 and freq[s] > 0:
                            bad -= 1

                # Remove y from the window.
                freq[y] -= 1

                # If y no longer exists, it can no longer be
                # the third element of a violating triple.
                if freq[y] == 0 and pair_sum[y] > 0:
                    bad -= 1

                left += 1

            ans = max(ans, right - left + 1)

        return ans
