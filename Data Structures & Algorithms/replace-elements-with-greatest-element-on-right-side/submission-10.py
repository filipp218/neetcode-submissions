class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result = []
        for i in range(len(arr)):
            if len(result) + 1 == len(arr):
                result.append(-1)
            else:
                result.append(
                    max(arr[i+1:])
                )
        return result
            
        