class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Solving this via two pointers
        result = []

        for i in range(len(temperatures)):
            indicator = False
            count = 1
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    result.append(count)
                    indicator = True
                    break
                else:
                    count += 1
                    indicator = False

            if indicator == False:
                result.append(0)

        return result