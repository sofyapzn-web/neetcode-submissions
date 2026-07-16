from math import prod

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        output = [0]*l
        prodnums = prod(nums)
        for i in range(l):
            output[i] = prodnums // nums[i]
        return output