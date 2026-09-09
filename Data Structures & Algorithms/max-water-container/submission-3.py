class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights) -1 
        area = 0
        while start != end:
            distance = end - start
            area = max(distance*min(heights[start],heights[end]), area)
            if heights[start]<=heights[end]:
                start += 1
            else: end -= 1
            print(area)
        return area

        