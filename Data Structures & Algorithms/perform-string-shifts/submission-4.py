class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        n = len(s)
        total = 0
        for direction, amount in shift:
            if direction == 1:
                total += amount
            else:
                total -= amount

        total %= n
        return s[n - total:] + s[:n - total]


        