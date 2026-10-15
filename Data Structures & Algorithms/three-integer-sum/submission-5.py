class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sort_nums = sorted(nums)
        result = []
        for i in range(len(sort_nums)):
            if i > 0 and sort_nums[i] == sort_nums[i - 1]:
                continue
            start = sort_nums[i]
            left_border = i + 1
            right_border = len(sort_nums) - 1

            while right_border > left_border:
                sum3 = start + sort_nums[left_border] + sort_nums[right_border]
                if sum3 == 0:
                    result.append(
                        [start, sort_nums[left_border], sort_nums[right_border]]
                    )
                    right_border -= 1
                    left_border += 1
                    while right_border > left_border and sort_nums[left_border] == sort_nums[left_border - 1]:
                        left_border += 1

                elif sum3 > 0:
                    right_border -= 1
                else:
                    left_border += 1
        return result
        