class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        # Sliding window algorithm
        left, right, result = 0, 0, 0

        for right in range(len(prices)):
            if prices[left] > prices[right]:
                left = right
            else:
                profit = prices[right] - prices[left]
                result = max(result, profit)
        
        return result