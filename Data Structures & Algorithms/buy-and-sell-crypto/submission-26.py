class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # If it is SLIDING WINDOW algoritm: left and right pointers will start from 0's index
        left, right = 0, 0
        maxProfit = 0
        while right < len(prices):
            if prices[left] > prices[right]:
                left = right
            else:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
            right += 1
        
        return maxProfit