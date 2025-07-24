class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minimum = prices[0]
        for i in range(1, len(prices)):
            if profit < (prices[i] - minimum):
                profit = prices[i] - minimum
            elif prices[i] < minimum:
                minimum = prices[i]

        return profit
