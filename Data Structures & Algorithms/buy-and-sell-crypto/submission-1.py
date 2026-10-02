class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        # profit = (element2 - elemnt 1)
        result = 0

        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                result = max(profit, result)
        
        return result