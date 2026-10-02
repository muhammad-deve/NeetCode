from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)

        for element in strs:
            freq_list = [0] * 26

            for ch in element:
                freq_list[ord(ch) - ord('a')] += 1

            hash_map[tuple(freq_list)].append(element)

        return list(hash_map.values())