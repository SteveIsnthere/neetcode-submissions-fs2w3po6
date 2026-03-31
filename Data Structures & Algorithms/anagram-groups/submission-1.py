class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}

        def str_sort(s: str) -> str:
            sl = []
            for c in s:
                sl.append(c)
            sl.sort()

            res = ""
            for c in sl:
                res += c
            return res

        for i in range(len(strs)):
            s = strs[i]
            sorted_s = str_sort(s)
            if sorted_s in hm.keys() and hm[sorted_s]:
                hm[sorted_s].append(i)
            else:
                hm[sorted_s] = [i]
        
        keys = hm.keys()
        res = []

        for k in keys:
            idxs = hm[k]
            group = []
            for idx in idxs:
                group.append(strs[idx])
            res.append(group)

        return res
            
