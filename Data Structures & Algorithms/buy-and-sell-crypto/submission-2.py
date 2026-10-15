class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = prices[0]
        max_val = 0
        profit = 0
        for num in prices:
            if num <= min_val:
                profit = max(profit, max_val - min_val)
                min_val = num
                max_val = 0
            else:
                max_val = max(max_val, num)
        profit = max(profit, max_val - min_val)

        return profit
            