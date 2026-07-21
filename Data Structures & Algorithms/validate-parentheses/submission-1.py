
class Solution:
    def isValid(self, s: str) -> bool:
        CTO = {')':'(', '}':'{', ']':'['}
        stack =[]
        for ss in s:
            if ss in CTO :
                if stack and stack[-1]==CTO[ss]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ss)
        return True if not stack else False
            






