# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buyDay = 0
        profit = []
        for day in range(1,len(prices)):
            sellDay = day
            if prices[buyDay] < prices[sellDay]:
                profit.append(prices[sellDay]-prices[buyDay])
            elif prices[buyDay] > prices[sellDay]:
                buyDay = sellDay
        if profit != []:
            return max(profit)
        else:
            return 0