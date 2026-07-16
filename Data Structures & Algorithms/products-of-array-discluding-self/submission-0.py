class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        output = [0]*l
        sumnums = sum(nums)
        for i in range(l):
            output[i] = sumnums - nums[i]
        return output