from collections import defaultdict
    
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs ==[''] or len(strs) == 1 :
            return [strs]
        d = {}
        cnt = [0]*26
        for i, n in enumerate(strs):
            for j in strs[i]:
                cnt[ord(j)-ord('a')] += 1
            count = tuple(cnt)
            if count in d :
                d[count].append(n)
            else :
                d[count] = [n]
            cnt = [0]*26
        sol = []
        for x in d.values():
            sol.append(x)
        return sol
                
