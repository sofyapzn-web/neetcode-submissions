from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        r = len(nums)
        cnt = 0
        d = defaultdict(list)
        for i in range(r):
            for j in range(r):
                for k in range(r):
                    ni = nums[i]
                    nj=nums[j]
                    nl = nums[k]
                    if ni!=nj and nj!=nk and ni+nj+nk==0:
                        d[cnt].append([nj,ni,nk])
                        cnt+=1
        s = []
        for x in d.values():
            sx = sorted(x)
            if sx not in s :
                s.append(sx)