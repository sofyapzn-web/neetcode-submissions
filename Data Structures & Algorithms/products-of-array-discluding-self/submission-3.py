from math import prod

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        if 0 in nums :
            sol = [0]*l
            i = nums.index(0)
            sol[i]= prod(nums[:i])*prod(nums[i+1:])
            return sol
        else:
            output = [0]*l
            prodnums = prod(nums)
            for i in range(l):
                output[i] = prodnums // nums[i]
        return output