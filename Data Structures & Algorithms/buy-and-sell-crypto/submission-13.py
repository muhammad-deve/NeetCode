class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        left, right, maxProfit = 0, 0, 0

        for right in range(len(prices)):
            if prices[left] > prices[right]:
                left = right
            else:
                profit = prices[right] - prices[left]
                maxProfit = max(profit, maxProfit)
                right += 1

        return maxProfit