class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ''
        for x in s :
            if x.isalnum():
                st += x
        l = len(st)
        for i in range(l):
            if st[-1-i]!=st[i]:
                return False
        return True
