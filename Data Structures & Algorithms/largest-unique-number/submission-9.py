class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        exists = set()
        unique = set()
        for num in nums:
            if num not in exists:
                exists.add(num)
                unique.add(num)
                continue
            if num in unique:
                unique.remove(num)

        if not unique:
            return -1
        return max(unique)