class Solution(object):
    def isPalindrome(self, n):
        dup = n
        rev=0
        while(n>0):
            lastdigit = n%10
            rev = rev*10 + lastdigit
            n= n//10

        if(rev == dup):
            return True
        else:
            return False
        
