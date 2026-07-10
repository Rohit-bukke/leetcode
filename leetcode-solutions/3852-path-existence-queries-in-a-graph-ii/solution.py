class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        LOG = 18
        vec = []
        for i in range(n):
            vec.append((nums[i], i))
        vec.sort()

        getSortIdx = [0] * n
        for i in range(n):
            getSortIdx[vec[i][1]] = i

        st = [[0] * LOG for _ in range(n)]
        l = 0

        for r in range(n):
            while vec[r][0] - vec[l][0] > maxDiff:
                st[l][0] = r - 1
                l += 1

        while l < n:
            st[l][0] = n - 1
            l += 1

        for j in range(1, LOG):
            for i in range(n):
                st[i][j] = st[st[i][j - 1]][j - 1]

        ans = [-1] * len(queries)

        for i in range(len(queries)):
            a = getSortIdx[queries[i][0]]
            b = getSortIdx[queries[i][1]]

            if a > b:
                a, b = b, a
            if a == b:
                ans[i] = 0
                continue

            cur = a
            step = 0

            for j in range(LOG - 1, -1, -1):
                if st[cur][j] < b:
                    step += 1 << j
                    cur = st[cur][j]

            if st[cur][0] >= b:
                ans[i] = step + 1

        return ans
        
