class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def k_finish(k):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)

            return hours <= h

        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2

            if k_finish(mid):
                right = mid
            else:
                left = mid + 1
        
        return left