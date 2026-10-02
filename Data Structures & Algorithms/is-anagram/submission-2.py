class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        MapS = {}
        MapT = {}

        for i in range(len(s)):
            MapS[s[i]] = MapS.get(s[i], 0) + 1
            MapT[t[i]] = MapT.get(t[i], 0) + 1

        return MapS == MapT