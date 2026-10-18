class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq = 0
        left_border = 0
        counter = dict()
        res = 0
        for right_border in range(len(s)):
            counter[s[right_border]] = counter.get(s[right_border], 0) + 1
            max_freq = max(max_freq, counter[s[right_border]])
            if right_border - left_border + 1 - max_freq > k:
                counter[s[left_border]] -= 1
                left_border += 1
            
            res = max(right_border - left_border + 1, res)
        return res


        