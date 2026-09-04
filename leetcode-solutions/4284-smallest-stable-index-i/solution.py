class Solution:
    def firstStableIndex(self, a: list[int], k: int) -> int:
        return next((i for i in range(len(a)) if max(a[:i+1])-min(a[i:])<=k),-1)
