class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen_nums = set()
        max_len = 0
        set_nums = set(nums)
        for num in nums:
            if num in seen_nums:
                continue
            cur_len = 1
            move_left = num - 1
            while move_left in set_nums:
                seen_nums.add(move_left)
                move_left -= 1
                cur_len += 1
            move_right = num + 1
            while move_right in set_nums:
                seen_nums.add(move_right)
                move_right += 1
                cur_len += 1
            max_len = max(max_len, cur_len)

        return max_len
            

            
        