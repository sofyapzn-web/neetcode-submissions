class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        x = 0
        bracket=[]
        for i, n in enumerate(tokens):
            while isdigit(n):
                bracket.append(int(n))
            break
            if tokens[i+1] == '+':
                for s in bracket:
                    x +=s
            elif tockens[i+1] == '-':
                for s in bracket:
                    x -= s
            elif tockens[i+1] == '*':
                for s in bracket:
                    x*s
            elif tockens[i+1] == '/':
                for s in bracket:
                    x // s
            return x
            
                