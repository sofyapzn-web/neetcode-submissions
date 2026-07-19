class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left =0
        right = len(heights)-1
        maximum = 0
        while left < right :
            hleft = heights[left]
            hright = heights[right]
            area = min(hleft, hright)*(right-left) 
            if area > maximum :
                maximum = area
            if hleft<=hright:
                left += 1
            elif hright<hleft:
                right-=1
        return maximum