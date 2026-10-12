class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = []
        cur_num = 1
        for num in nums:
            prefix.append(cur_num)
            cur_num *= num

        suffix = []
        cur_num = 1
        index = len(nums) - 1
        while index >= 0:
            suffix.append(cur_num)
            cur_num *= nums[index]
            index -= 1
        result = []
        for i in range(len(nums)):
            result.append(prefix[i] * suffix[len(nums) - i - 1])
        
        return result


