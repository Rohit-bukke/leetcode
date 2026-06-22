class Solution(object):
    def maxNumberOfBalloons(self, text):
        target="balloon"
        freq={}
        for i in text:
            if i in target:
                freq[i]=freq.get(i,0)+1
        return min(
            freq.get('b',0),
            freq.get('a',0),
            freq.get('l',0)//2,
            freq.get('o',0)//2,
            freq.get('n',0)
        )

        
