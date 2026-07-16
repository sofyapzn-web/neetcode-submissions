class Solution:

    def encode(self, strs: List[str]) -> str:
        sol = ''
        for s in strs :
            sol += str(len(s)) + s
        return sol

    def decode(self, s: str) -> List[str]:
        l = []
        while s!='':
            l.append(s[1 : s[0]+2])
            s = s[s[0]+1:]
        return l
