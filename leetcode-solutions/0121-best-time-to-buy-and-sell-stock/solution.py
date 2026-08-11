class Solution(object):
    def maxProfit(self, prices):
        minprice=float("INF")
        maxprofit=0
        for price in prices:
            minprice=min(minprice,price)
            profit=price-minprice
            maxprofit=max(maxprofit,profit)
        return maxprofit

        
