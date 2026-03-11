class Solution(object):
    def reverse(self, x):
        sign=-1 if x<0 else 1
        x=abs(x)
        rev=0
        while(x>0):
            lastdigit= x%10
            rev= (rev*10)+lastdigit
            x= x//10
        final_result= sign*rev
        if final_result < -2**31 or final_result > 2**31 - 1:
            return 0
        return final_result
