class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for word in strs:
            res += f'{len(word)}#{word}'
        return res

    def decode(self, s: str) -> List[str]:
        res = []; i = 0; n = len(s)
        while i < n:
            number = ''
            while '0' <= s[i] <= '9':
                number += s[i]
                i += 1
            if s[i] == '#':
                i += 1
            res.append(s[i:i + int(number)])
            i += int(number)
        return res
