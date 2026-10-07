class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        len_word = 0
        right_border = len(s) - 1
        start = False
        while right_border >= 0:

            if start and not s[right_border].isalpha():
                return len_word
    
            if s[right_border].isalpha():
                start = True
                len_word += 1
            right_border -= 1
            
        return len_word
        