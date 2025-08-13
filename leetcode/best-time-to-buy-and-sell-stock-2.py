class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        bought_stock = prices[0]
        for i in range(1, len(prices)):
            # Sell
            if prices[i] - bought_stock > 0:
                profit += prices[i] - bought_stock
                bought_stock = prices[i]
            
            # Buy
            elif bought_stock > prices[i]:
                bought_stock = prices[i]
        
        return profit
