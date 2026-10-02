class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        # Brute Force
        left, right = 0, 1
        maxProfit = 0
        
        while left < len(prices) - 1:
            profit = prices[right] - prices[left]
            maxProfit = max(profit, maxProfit)
            
            if right == len(prices) - 1:
                left += 1
                right = left + 1
            elif right < len(prices):
                right += 1
        
        return maxProfit