class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        days = len(prices)
        index = 1
        for i in prices:
            buy = i
            for j in range(index,days):
                sell = prices[j]
                if sell<=buy: continue
                else:
                    cur_profit = sell-buy
                    profit = cur_profit if profit<cur_profit else profit
            index +=1
        return profit


        