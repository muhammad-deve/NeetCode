class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def k_finish(k):
            hours_needed = 0
            for pile in piles:
                hours_needed += math.ceil(pile / k)
            
            return h >= hours_needed
        
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2

            if k_finish(mid):
                right = mid
            else:
                left = mid + 1

        return right