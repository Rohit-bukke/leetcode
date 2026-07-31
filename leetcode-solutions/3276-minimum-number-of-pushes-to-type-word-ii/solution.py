class Solution:
    def minimumPushes(self, word: str) -> int:
        ct = Counter(word)
        hm = list(ct.values())
        hm.sort(reverse=True)
        s = 0
        for i,v in enumerate(hm):
            s+=v
            if i>7:
                s+=v
            if i>15:
                s+=v
            if i>23:
                s+=v
        return s
