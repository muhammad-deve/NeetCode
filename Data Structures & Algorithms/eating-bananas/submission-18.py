class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        We are going to use Binary searh to reach O(logn)
        we check if KOKO can finish within given hour(h)
        """

        def k_finish(k): # We will check if rate K is going to be enoug
            hours = 0 # How long does it take to finish piles with given K rate
            for pile in piles:
                hours += math.ceil(pile / k)
            
            # Return if hours is smaller than given h
            return hours <= h
        

        # Left pointer is going to be 1 and Right pointer will be Max of the elemets
        left, right = 1, max(piles)
        # Do not put '=' because if there is only one elemnet it get stuck
        while left < right:
            mid = (left + right) // 2
            
            if k_finish(mid):
                right = mid
            else:
                left = mid + 1 # If mid does not work we don't need mid
        
        return left