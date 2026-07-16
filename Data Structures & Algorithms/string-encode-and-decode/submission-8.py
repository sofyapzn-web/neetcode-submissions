class Solution:

    def encode(self, strs: List[str]) -> str:
        sol = ''
        for s in strs :
            sol += str(len(s)) + '#' + s
        return sol

    def decode(self, s: str) -> List[str]:
        l = []
        while s!='':
            for i, n in enumerate(s) :
                if n == '#':
                    ii = int(s[:i])
                    l.append(s[i+1 : ii+ i +1])
            s = s[ii+i+1:]
        return l
