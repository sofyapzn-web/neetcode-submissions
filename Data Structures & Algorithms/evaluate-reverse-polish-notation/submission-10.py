class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        r = len(tokens)
        for n in tokens:
            if n.isdigit():
                stack.append(n)
            else :
                if n == '+':
                    for i in range(1,r):
                        stack[0] = int(stack[0])+int(stack[i])
                        stack = [stack[0]]
                elif n == '-':
                    for i in range(1,r) :
                        stack[0] = int(stack[0])-int(stack[i])
                        stack = [stack[0]]
                elif n == '*':
                    for i in range(1,r) :
                        stack[0] = int(stack[0])*int(stack[i])
                        stack = [stack[0]]
                elif n == '/':
                    for i in range(1, r):
                        stack[0]= int(stack[0])//int(stack[i])
                        stack = stack[0]
                return stack[0]