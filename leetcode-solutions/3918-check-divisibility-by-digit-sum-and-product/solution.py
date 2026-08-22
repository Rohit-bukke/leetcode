class Solution(object):
    def checkDivisibility(self, n):
        sum=0
        prod=1
        temp=n
        while(temp>0):
            digit=temp%10
            sum=sum+digit
            prod=prod*digit
            temp=temp//10
        total_sum=sum+prod
        if(n%total_sum==0):
            return True
        return False

