class Solution:
    def sumAndMultiply(self, n):
        x = 0
        total_sum = 0
        length = 1

        while n != 0:
            digit = n % 10
            x = digit * length + x

            if digit != 0:
                length *= 10

            total_sum += digit
            n //= 10

        return total_sum * x
