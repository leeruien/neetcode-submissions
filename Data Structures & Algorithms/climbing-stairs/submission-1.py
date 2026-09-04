class Solution:
    def climbStairs(self, n: int) -> int:
        store = [1,2,3,5]
        if n<=4:
            return store[n-1]
        for i in range(4,n):
            store.append(store[i-1] + store[i-2])
        return store[-1]        