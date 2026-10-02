class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # This function checks if KOKO finish or not
        def k_finish(k):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            
            return hours <= h
        
        left, right = 1, max(piles)
        result = right
        
        while left < right:
            mid = (left + right) // 2
            if k_finish(mid):
                result = min(mid, result)
                right = mid
            else:
                left = mid + 1
        return result