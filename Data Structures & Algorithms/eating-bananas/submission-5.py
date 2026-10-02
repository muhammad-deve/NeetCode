class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        result = right  # Because at least the max value will work

        while left <= right:
            mid = (left + right) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / mid) # Make the number
            
            if hours <= h:
                result = min(result, mid)  # Fixed: should be mid, not h
                right = mid - 1
            else:
                left = mid + 1
            
        return result