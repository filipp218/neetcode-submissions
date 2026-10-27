class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def binary_search(left, right, target, nums):
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            if left > right:
                return - 1
            
            if nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1
            return binary_search(left, right, target, nums)

        return binary_search(0, len(nums) - 1, target, nums)

        

        

        