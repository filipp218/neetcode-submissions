class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        from collections import Counter
        c_s = Counter(s)
        if len(list(filter(lambda x: c_s[x] % 2 == 1, c_s))) > 1:
            return False
        return True


        