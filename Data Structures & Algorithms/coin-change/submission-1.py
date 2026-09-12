class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        end = len(coins) - 1
        num_coins = [10001]*(amount+1)
        sorted_coins = sorted(coins)
        for i in range(1,amount + 1):
            min_coins = 10001
            for j in sorted_coins:
                if j > i: break
                elif i == j: 
                    num_coins[i] = 1
                    break
                else:
                    min_coins = min(num_coins[i-j]+1, min_coins)
                    num_coins[i] = min_coins
        if num_coins[-1] == 10001: return -1
        return num_coins[-1]