class Solution:
    def confusingNumber(self, n: int) -> bool:
        rotating_number = []
        mapping = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6',
        }
        for char in str(n):
            if char not in mapping:
                return False
            if mapping[char] == 0 and not rotating_number:
                continue

            rotating_number.append(mapping[char])
        
        return n != int(''.join(reversed(rotating_number)))
