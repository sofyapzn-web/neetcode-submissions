from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for n in nums:
            d[n]+=1
        sorted_items= sorted(d.items(), key = lambda item : item[1], reverse= True)
        sol = []
        for i in range(k):
            for j in sorted_items[i]:
                sol.append(j[0])
        return sol


            
