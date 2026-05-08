class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n: int = len(s)
        if n <= 1: return n
        seen: set = set()
        max_sequence: int = 0
        l: int = 0 
        r: int = 0
        while r < n:
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            max_sequence = max(max_sequence, r - l + 1)
            r += 1
        return max_sequence