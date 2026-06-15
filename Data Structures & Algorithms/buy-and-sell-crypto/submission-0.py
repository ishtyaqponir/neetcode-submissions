class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        if len(prices) == 1:
            return 0
        #Brute Force
        maxProfit = 0
        for i in range(len(prices)):
            for j in range (i+1, len(prices)):
                curProfit = prices[j] - prices[i]
                if curProfit > maxProfit:
                    maxProfit = curProfit
        return maxProfit
        