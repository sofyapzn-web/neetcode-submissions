class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = []
        if len(s) != len(t):
            return False
        for i in s:
            seen.append(i)
        for j in t :
            if j not in seen :
                return False
            seen.remove(j)
        return True
