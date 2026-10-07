class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        left_border_s = 0
        left_border_t = 0
        while left_border_s < len(s) and left_border_t < len(t):
            if s[left_border_s] == t[left_border_t]:
                left_border_s += 1
                left_border_t += 1
            else:
                left_border_s += 1

        return len(t) - left_border_t

        