class Solution:
    def zigZagArrays(self, n, l, r):
        MOD = 10**9 + 7

        m = r - l + 1

        up = [0] * (m + 1)
        down = [0] * (m + 1)

        # length = 2
        for x in range(1, m + 1):
            up[x] = x - 1          # values smaller than x
            down[x] = m - x        # values greater than x

        # build lengths 3..n
        for _ in range(3, n + 1):

            pref_up = [0] * (m + 1)
            pref_down = [0] * (m + 1)

            for i in range(1, m + 1):
                pref_up[i] = (pref_up[i - 1] + up[i]) % MOD
                pref_down[i] = (pref_down[i - 1] + down[i]) % MOD

            new_up = [0] * (m + 1)
            new_down = [0] * (m + 1)

            total_up = pref_up[m]

            for x in range(1, m + 1):

                # previous move was DOWN
                new_up[x] = pref_down[x - 1]

                # previous move was UP
                new_down[x] = (total_up - pref_up[x]) % MOD

            up = new_up
            down = new_down

        ans = (sum(up) + sum(down)) % MOD
        return ans
