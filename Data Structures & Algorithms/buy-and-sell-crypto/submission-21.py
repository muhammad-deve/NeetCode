class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 0
        maxProfit = 0

        while right < len(prices):
            # If profitable:
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
            # If not profitable
            else:
                left = right

            right += 1

        return maxProfit

