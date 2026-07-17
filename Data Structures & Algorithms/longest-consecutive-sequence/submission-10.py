from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        if len(nums)==1:
            return 1
        d = defaultdict(lambda : 1)
        n = 0
        sortnums = sorted(nums)
        for i in range(1,len(sortnums)) :
            if sortnums[i] == sortnums[i-1]:
                continue
            elif sortnums[i] == sortnums[i-1] + 1:
                d[n]+=1
            else:
                n+=1
        return max(d.values())+1