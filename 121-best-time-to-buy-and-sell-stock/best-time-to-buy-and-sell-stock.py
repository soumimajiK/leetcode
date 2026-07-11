class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        actualprof=0
        buy=prices[0]
        for i in range(len(prices)):
            profit=prices[i]-buy
            actualprof = max(actualprof, profit)
            buy=min(buy, prices[i])
        return actualprof
        