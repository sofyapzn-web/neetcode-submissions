from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        r = len(nums)
        res=[]
        for i in range(r):
            mid = i
            left = i+1
            right = -1
            while left<right :
                if nums[left]+nums[right] > -nums[mid]:
                    right-=1
                elif nums[left]+nums[right] < -nums[mid]:
                    left +=1
                else :
                    s = sorted([nums[left], nums[right], nums[mid]]) 
                    if s not in res and left != right and right!=mid :
                        res.append(s)
        return res
