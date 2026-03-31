from copy import deepcopy

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hm = {}
        for i,n in enumerate(nums):
            if n in hm.keys():
                hm[n].append(i)
            else:
                hm[n] = [i]


        r = []
        for i,n in enumerate(nums):
            thm = deepcopy(hm)
            new_list = []
            for item in thm[n]:
                if item != i:
                    new_list.append(item)
            thm[n] = new_list

            rnum = -n
            for ix, num in enumerate(nums):
                if ix <= i: continue
                diff = rnum - num
                new_list = []
                for item in thm[num]:
                    if item != ix:
                        new_list.append(item)
                thm[num] = new_list
                if diff in thm.keys() and len(thm[diff]) > 0:
                    res = [n,num,diff]
                    res.sort()
                    r.append(res)
        
        fr = []
        for i in r:
            if i not in fr:
                fr.append(i)
        return fr