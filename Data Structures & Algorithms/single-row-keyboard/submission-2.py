class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        mapping = {
            char: index for index, char in enumerate(keyboard)
        }
        previus = 0
        total = 0


        for char in word:
            cur = mapping[char]
            total += abs(previus - cur)
            previus = cur
        return total
