class Solution(object):
    def processStr(self, s, k):

        length = 0

        # Find final length
        for ch in s:
            if ch.isalpha():
                length += 1

            elif ch == "*":
                if length > 0:
                    length -= 1

            elif ch == "#":
                length *= 2

        if k >= length:
            return '.'

        # Work backwards
        for ch in reversed(s):

            if ch.isalpha():

                length -= 1

                if k == length:
                    return ch

            elif ch == "*":

                length += 1

            elif ch == "#":

                length //= 2
                k %= length

            elif ch == "%":

                k = length - 1 - k


# class Solution(object):
#     def processStr(self, s, k):
#         result=[]
#         for ch in s:
#             if ch.isalpha():
#                 result.append(ch)
#             elif(ch=="*"):
#                 if result:   # result means list is not empty
#                     result.pop()
#             elif(ch=="%"):
#                 result.reverse()
#             elif ch=="#":
#                 result.extend(result)
#         final_str="".join(result)
#         if k<len(final_str):
#             return final_str[k]
#         return '.' 
            
