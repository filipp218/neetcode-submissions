class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        count_nums = Counter(nums)
        key_value = [(value, key) for key, value in count_nums.items()]
        sorted_key_value = sorted(key_value, key=lambda x: x[0], reverse=True)
        result = sorted_key_value[:k]
        return [key for value, key in result]


        