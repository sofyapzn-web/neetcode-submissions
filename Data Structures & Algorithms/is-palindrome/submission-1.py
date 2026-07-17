class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = s.lower()
        st = st.strip()
        st= ''.join(st)
        l = len(s)
        for i in range(l):
            if st[-i-1] != st[i]:
                return False
        return True
