class Solution:
    def trap(self, height: List[int]) -> int:
        lrmax = {}
        r = len(height)
        area=0
        for i in range(r):
            if i == 0:
                lrmax[0]=(0, max(height[-1-i::-1]))
            elif i ==r-1:
                lrmax[i]=(max(height[:i]), 0)
            else:
                lrmax[i]=(max(height[:i]), max(height[-1-i::-1]))

        for i in range(r):
            areatoadd=min(lrmax[i])-height[i]
            if aretoadd >0 :
                area += areatoadd

        return area

                

