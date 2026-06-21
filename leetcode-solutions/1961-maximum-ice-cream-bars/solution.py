class Solution(object):
    def maxIceCream(self, costs, coins):

        costs.sort()

        count = 0

        for cost in costs:
            if coins >= cost:
                coins -= cost
                count += 1
            else:
                break

        return count


# #with freqency 
# class Solution(object):
#     def maxIceCream(self, costs, coins):
#         maxcost = max(costs)
#         n = maxcost + 1

#         freq = [0] * n

#         for cost in costs:
#             freq[cost] += 1

#         count = 0

#         for i in range(1, n):
#             while freq[i] > 0:
#                 if coins >= i:
#                     coins -= i
#                     count += 1
#                     freq[i] -= 1
#                 else:
#                     return count

#         return count
