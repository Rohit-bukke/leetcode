class Solution(object):
    def maxProfit(self, prices):
        #optimal approach only becasue bruite force does not work
        maxprofit=0
        minprice=float("INF")
        for i in range(len(prices)):
            minprice=min(prices[i],minprice)
            maxprofit=max(prices[i]-minprice,maxprofit)
        return maxprofit

        
