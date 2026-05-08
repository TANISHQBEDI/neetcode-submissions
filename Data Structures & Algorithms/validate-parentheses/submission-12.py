class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        m = {'}':'{', ')':'(', ']':'['}
        for bracket in s:
            if stack and bracket in m and m[bracket] == stack[-1]:
                stack.pop()
            else:
                stack.append(bracket)
        return len(stack) == 0