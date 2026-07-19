class Solution:
    def trap(self, height: List[int]) -> int:
        lrmacx = {}
        r = len(height)
        area=0
        for i in range(r):
            lrmax[i]=(max(height[:i]), max(height[-1-i::-1]))

        for i in range(r):
            areatoadd=min(lrmax[i])-height[i]
            if aretoadd >0 :
                area += areatoadd

        return area

                

