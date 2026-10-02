class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 0
        maxProfit = 0

        while right < len(prices):
            # If the transaction is profitable
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxProfit = max(profit, maxProfit)
            # If the transaction is not profitable
            else:
                left = right
            
            right += 1
        
        return maxProfit
