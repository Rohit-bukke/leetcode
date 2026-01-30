class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        while True:
            res = 0 ;
            while(num > 0):
                d = num%10;
                res += d;
                num /= 10;
            num = res
            if res < 10 :
                return res;
            
        return res;

