from collections import defaultdict
    
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs ==[''] or len(strs) == 1 :
            return [strs]
        d = {}
        cnt = [0]*26
        for i in strs:
            for j in strs[i]:
                cnt[ord(i)-ord('a')] += 1
            count = tuple(cnt)
            if count in d :
                d[count].append(i)
            else :
                d[count] = [i]
            cnt = [0]*26
        sol = []
        for x in d.values():
            sol.append(x)
        return sol
                
