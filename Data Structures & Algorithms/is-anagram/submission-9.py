class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sf = [0] * 26
        tf = [0] * 26
        for l in s:
            sf[ord(l) - ord('a')] += 1
        for l in t:
            tf[ord(l) - ord('a')] += 1
        return sf == tf