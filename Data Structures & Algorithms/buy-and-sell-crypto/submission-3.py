class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices is None:
            return 0
        start = 0
        end = 1
        mProfit = 0
        while end < len(prices):
            if prices[end] > prices[start]:
                mProfit = max(mProfit, prices[end] - prices[start])
            else:
                start = end # need this to be at the new lowest found
            end += 1
        return mProfit