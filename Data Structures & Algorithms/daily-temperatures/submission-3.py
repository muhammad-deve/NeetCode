class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            # Process all days that are waiting for a warmer temperature
            while len(stack) != 0 and stack[-1][1] < t:
                prev_index, prev_temp = stack.pop()
                result[prev_index] = i - prev_index
            
            stack.append([i, t])

        return result