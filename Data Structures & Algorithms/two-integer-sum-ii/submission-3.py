class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        cur_1 = 0
        cur_2 = len(numbers) - 1
        while cur_2 > cur_1:
            sum_curs = numbers[cur_1] + numbers[cur_2]
            if sum_curs > target:
                cur_2 -= 1
            elif sum_curs == target:
                return [cur_1+1, cur_2+1]
            else:
                cur_1 += 1