class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        for n in nums:
            if n in hm.keys():
                hm[n] += 1
            else:
                hm[n] = 1
        res = []
        for key in hm.keys():
            res.append([key, hm[key]])
            
        res.sort(key=lambda x: -x[1])

        res = res[:k]
        r = []
        for n in res:
            r.append(n[0])

        return r