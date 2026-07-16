class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 1 :
            return strs[0]
        sol = ''
        for s in strs :
            sol += str(len(s)) + '#' + s
        return sol

    def decode(self, s: str) -> List[str]:
        l = []
        while s!='':
            for i, n in enumerate(s) :
                if n == '#':
                    length = int(s[:i])
                    l.append(s[i+1: length+i+1])
                    s = s[length+i+1:]
        return l