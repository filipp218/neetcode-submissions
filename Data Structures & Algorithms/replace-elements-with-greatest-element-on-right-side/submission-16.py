1, 2, 3
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result = [-1]
        right_border = len(arr) - 1
        max_num = arr[right_border]
        while right_border > 0:
            result.append(max_num)
            right_border -= 1
            max_num = max(max_num, arr[right_border])

        return list(reversed(result))