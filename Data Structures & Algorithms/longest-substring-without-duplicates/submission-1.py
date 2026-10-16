class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set_exist = set()
        max_len = 0
        if len(s) < 2:
            return len(set(s))

        left_border, right_border = 0, 1
        set_exist.add(s[left_border])

        while right_border < len(s):
            if s[right_border] not in set_exist:
                set_exist.add(s[right_border])
                right_border += 1
            else:
                set_exist.remove(s[left_border])
                left_border += 1

            max_len = max(max_len, len(set_exist))
    
        return max_len
            
        