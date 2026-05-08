class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)
        for s in strs:
            key = sorted([l for l in s])
            key = ''.join(key)
            m[key].append(s)
        print(m)
        return [val for val in m.values()]
        