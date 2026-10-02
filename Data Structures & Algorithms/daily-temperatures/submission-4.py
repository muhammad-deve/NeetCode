class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        result = [0] * len(temperatures)
        stack = [] # index: element

        for index, element in enumerate(temperatures):
            while len(stack) != 0 and stack[-1][1] < element:
                prev_index, prev_element = stack.pop()
                result[prev_index] = index - prev_index
            
            stack.append([index, element])
        
        return result
