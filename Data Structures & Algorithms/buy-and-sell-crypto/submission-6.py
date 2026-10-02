class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        """
        Optimal solution using SLIDING WINDOW algorithm
        In here instead of checking every combination 
        I check if the right element is less than left elemnet
        If so i will move my LEFT pointer to buy CHEAPER stock
        """
        left, right = 0, 1
        maxProfit = 0

        while left < len(prices) - 1:
            if right < len(prices) - 1:
                if prices[left] >= prices[right]:
                    left += 1
                    right = left + 1
                else:
                    profit = prices[right] - prices[left]
                    maxProfit = max(maxProfit, profit)
                    right += 1
            else:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
                left += 1
                right = left + 1

        return maxProfit