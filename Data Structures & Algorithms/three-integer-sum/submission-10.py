from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        r = len(nums)
        res=[]
        nums.sort()
        for i in range(r):
            if i>0 and nums[i]== nums[i-1]:
                continue
            mid = i
            left = i+1
            right = r-1
            while left<right :
                total = nums[mid] + nums[left] + nums[right]
                if total>0 :
                    right -=1
                elif total<0 :
                    left+=1
                else :
                    res.append([nums[mid], nums[left], nums[right]])
                    right-=1
                    left+=1
                    while left<right and num[right+1]==nums[right]:
                        right-=1
                    while left< right and num[left-1]==nums[left]:
                        left += 1
        return res

