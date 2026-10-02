class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        """
        Optimal solution using SLIDING WINDOW algorithm
        In here instead of checking every combination 
        I check if the right element is less than left element
        If so i will move my LEFT pointer to buy CHEAPER stock
        """
        left, right = 0, 1
        maxProfit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
            else:
                left = right
            
            right += 1

        return maxProfit

        # Time complexity: O(n) - each pointer moves forward only once
        # Space complexity: O(1) - only using constant extra space