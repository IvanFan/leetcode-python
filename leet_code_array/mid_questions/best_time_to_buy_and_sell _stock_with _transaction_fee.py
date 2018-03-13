class Solution:
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        cash = 0
        hold = -prices[0]
        for day in range(1, len(prices)):
            yesterdayCash = cash
            cash = max(yesterdayCash, hold + prices[day] - fee)
            hold = max(hold, yesterdayCash-prices[day])
        return cash
        