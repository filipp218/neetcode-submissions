class Solution:
    def countElements(self, arr: List[int]) -> int:
        from collections import Counter
        arr_counter = Counter(arr)
        result = 0
        for num in arr:
            neibour = num + 1
            if neibour in arr_counter:
                result += 1
        return result