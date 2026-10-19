class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_sym = {'(': ')', '{': '}', '[': ']'}
        for sym in s:
            if sym not in open_sym and not stack:
                return False
            if sym not in open_sym:
                last_close = stack.pop()
                if last_close != sym:
                    return False
            else:
                stack.append(open_sym[sym])
        if not stack:
            return True
        return False
