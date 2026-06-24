class Solution(object):
    MOD = 1000000007

    def mul(self, a, b):
        n = len(a)
        m = len(b[0])

        res = [[0] * m for _ in range(n)]

        for i in range(n):
            for k in range(len(a[0])):
                if a[i][k] == 0:
                    continue

                for j in range(m):
                    res[i][j] = (res[i][j] + a[i][k] * b[k][j]) % self.MOD

        return res

    def powMul(self, base, exp, res):
        while exp > 0:
            if exp & 1:
                res = self.mul(res, base)

            base = self.mul(base, base)
            exp >>= 1

        return res

    def zigZagArrays(self, n, l, r):
        m = r - l + 1

        size = 2 * m

        u = [[0] * size for _ in range(size)]

        for i in range(m):
            for j in range(i):
                u[i][j + m] = 1

            for j in range(i + 1, m):
                u[i + m][j] = 1

        dp = [[1] * size]

        dp = self.powMul(u, n - 1, dp)

        ans = 0

        for i in range(size):
            ans = (ans + dp[0][i]) % self.MOD

        return ans
