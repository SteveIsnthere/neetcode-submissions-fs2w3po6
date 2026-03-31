class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0

        acc = set()
        l = 0
        r = 1
        acc.add(s[0])

        res = 1
        while r < len(s):
            c_c = s[r]
            while c_c in acc:
                acc.remove(s[l])
                l += 1
            _res = r-l+1
            if _res > res: res = _res
            r += 1
            acc.add(c_c)
        return res
