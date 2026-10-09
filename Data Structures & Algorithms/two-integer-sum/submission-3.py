class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_index = dict()
        for i in range(len(nums)):
             val_index.setdefault(nums[i], set())
             val_index[nums[i]].add(i)

        for i in range(len(nums)):
            need = target - nums[i]
            if need not in val_index:
                continue
            
            indexes = val_index[need]
            result = indexes - {i}
            if result:
                return [i, min(result)]
            
            
