from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for n in nums:
            d[n]+=1
        sorted_items= sorted(d.items(), key = lambda item : item[1], reverse= True)
        sol = []
        for i in range(k):
            sol.append(sorted_items[i][0])
        return sol


            
