class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        """
        Optimal solution using SLIDING WINDOW algorithm
        In here instead of checking every combination 
        I check if the right element is less than left element
        If so i will move my LEFT pointer to buy CHEAPER stock
        """
        left, right = 0, 0
        maxProfit = 0

        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
            else:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
                right += 1
        
        return maxProfit
        