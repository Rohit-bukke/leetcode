class Solution(object):
    def maxBuilding(self, n, restrictions):

        restrictions.sort(key=lambda x: x[0])

        length = len(restrictions)

        if length == 0:
            return n - 1

        is_last = restrictions[-1][0] == n

        m = length + 1 + (0 if is_last else 1)

        h = [[0, 0] for _ in range(m)]

        h[0] = [1, 0]

        # Left to Right pass
        for i in range(length):
            diff = restrictions[i][0] - h[i][0]
            reachable_height = h[i][1] + diff

            h[i + 1][0] = restrictions[i][0]
            h[i + 1][1] = min(reachable_height, restrictions[i][1])

        # Add building n if missing
        if not is_last:
            diff = n - h[length][0]
            reachable_height = h[length][1] + diff

            h[length + 1][0] = n
            h[length + 1][1] = min(reachable_height, n - 1)

        # Right to Left pass
        for i in range(m - 2, -1, -1):
            diff = h[i + 1][0] - h[i][0]
            reachable_height = h[i + 1][1] + diff

            h[i][1] = min(h[i][1], reachable_height)

        # Find maximum peak
        ans = 0

        for i in range(1, m):
            left_pos = h[i - 1][0]
            right_pos = h[i][0]

            left_height = h[i - 1][1]
            right_height = h[i][1]

            peak = ((right_pos - left_pos - abs(left_height - right_height)) // 2) + max(left_height, right_height)

            ans = max(ans, peak)

        return ans
