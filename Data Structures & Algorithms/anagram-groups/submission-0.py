from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anograms_dict = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            key = tuple(count)
            anograms_dict[key].append(s)

        answer = []
        for value in anograms_dict.values():
            answer.append(value)

        return answer