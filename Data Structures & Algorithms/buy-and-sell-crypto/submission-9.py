class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        """
        Optimal solution using SLIDING WINDOW algorithm
        In here instead of checking every combination 
        I check if the right element is less than left element
        If so i will move my LEFT pointer to buy CHEAPER stock
        """
        left, right = 0, 0
        result = 0

        while right < len(prices):
            if prices[left] > prices[right]:
                left = right
            else:
                result = max(result, prices[right] - prices[left])
            
            right += 1
        
        return result