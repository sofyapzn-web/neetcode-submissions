class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = len(numbers)
        for i in range(l):
            for j in range(l):
                if i != j and numbers[i]+numbers[j]==target :
                    return sorted([i+1, j+1])