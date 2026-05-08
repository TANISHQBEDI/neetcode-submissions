class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join([f'{len(word)}#{word}' for word in strs])

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
