class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        num_conseq = 1
        index = 0
        max_conseq = 1
        if nums ==[]: return 0
        for i in sorted_nums:
            if index == 0:
                index += 1
                prev = i
            else:
                if prev + 1 == i:
                    num_conseq += 1
                    max_conseq = num_conseq if num_conseq > max_conseq else max_conseq
                elif prev == i: continue
                else: num_conseq = 1
                prev = i
        return max_conseq
            

        