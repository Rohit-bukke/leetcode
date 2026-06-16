class Solution(object):
    def processStr(self, s):
        result = ""

        for ch in s:
            if ch.islower():          # append letter
                result += ch
            elif ch == "*":          # remove last character
                result = result[:-1]
            elif ch == "#":          # duplicate result
                result += result
            elif ch == "%":          # reverse result
                result = result[::-1]

        return result
