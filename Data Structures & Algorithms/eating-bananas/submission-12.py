class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # If you eat the bananas at this speed can you it finish off ?
        def k_works(k):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            
            return hours <= h
        
        left, right = 1, max(piles)
        
        while left < right:
            mid = (left + right) // 2
            if k_works(mid):
                right = mid
            else:
                left = mid + 1
        
        return left