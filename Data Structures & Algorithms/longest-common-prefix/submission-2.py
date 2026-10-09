class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        max_steps = len(min(strs))
        result = []
        
        for i in range(max_steps):
            unique = set()
            for let in strs:
                unique.add(let[i])
            if len(unique) == 1:
                result.append(list(unique)[0])
            else:
                return ''.join(result)
        return ''.join(result)