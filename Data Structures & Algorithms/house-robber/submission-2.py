class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length ==2: return max(nums[0], nums[1])
        if length >= 2:
            if nums[1]<nums[0]: store = [nums[0], nums[0]]
            else:
                store = [nums[0], nums[1]]
        else: 
            return nums[0]
        for i in range(2, length):
            store.append(max(nums[i]+store[i-2], store[i-1]))
        return store[-1]
