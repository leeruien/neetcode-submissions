class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for cur_index, cur_temp in enumerate(temperatures):
            while stack and cur_temp > stack[-1][0]:
                smaller_idx = stack.pop()[1]
                result[smaller_idx] = cur_index - smaller_idx
            stack.append((cur_temp, cur_index))
        return result
                    

        