class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        store=[cost[0]]
        if len(cost)>=2: store.append(cost[1])
        for i in range(2,len(cost)):
            curcost = min(store[i-1], store[i-2]) + cost[i]
            store.append(curcost)
        return min(store[-1], store[-2])
