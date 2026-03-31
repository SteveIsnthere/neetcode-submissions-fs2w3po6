class Solution:
    def isPalindrome(self, s: str) -> bool:
        c_s = ""
        for l in s:
            if l.isalnum():
                c_s += l

        c_s = c_s.lower()
        
        c_i = int(len(c_s) / 2)
        for i in range(c_i):
            if c_s[i] != c_s[len(c_s) - i - 1]: return False

        return True
        