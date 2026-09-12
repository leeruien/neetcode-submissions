class Solution:
    def canJump(self, nums: List[int]) -> bool:
        can_reach = [False] * len(nums)
        index = 0
        for i in nums:
            if index ==0:
                can_reach[0] = True
                if i <= len(nums) - 1:
                    for j in range(1,i+1):

                        can_reach[j] = True
                elif i >= len(nums): return True
            elif can_reach[index]:
                if index + i <= len(nums)-1:
                    for j in range(1,i+1):
                        can_reach[index+j] = True
                elif index + i > len(nums): return True
            index += 1
        return can_reach[-1]
            

        