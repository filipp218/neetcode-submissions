class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = float('inf')
        dp = [0] + [INF] * amount 

        for num in range(1, amount+1):
            for c in coins:
                if c <= num:
                    dp[num] = min(dp[num], dp[num - c] + 1)
    
        return dp[amount] if dp[amount] != float('inf') else -1
        