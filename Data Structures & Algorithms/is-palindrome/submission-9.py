class Solution:
    def isPalindrome(self, s: str) -> bool:

        num_alpha = []
        for char in s:
            if char.isalpha() or char.isdigit():
                num_alpha.append(char)
        left_cur = 0
        right_cur = len(num_alpha) - 1
        while right_cur >= left_cur:
            if num_alpha[left_cur].lower() != num_alpha[right_cur].lower():
                return False
            left_cur += 1
            right_cur -= 1
        return True
        