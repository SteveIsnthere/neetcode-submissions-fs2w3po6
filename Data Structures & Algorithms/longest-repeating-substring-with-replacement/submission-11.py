class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s: return 0

        l = 0
        r = 1
        hm = {}
        res = 1
        hm[s[l]] = 1
        
        while r < len(s):
            if s[r] in hm.keys():
                hm[s[r]] += 1
            else:
                hm[s[r]] = 1

            r_k = r-l+1 - max(hm.values())

            if r_k > k: 
                hm[s[l]] -= 1
                l += 1            
            res = max(r-l+1, res)
            r += 1
                
        return res
                