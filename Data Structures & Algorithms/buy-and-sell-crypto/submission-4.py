class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pl = 0
        pr = 1
        p = 0

        while pr < len(prices):
            l = prices[pl]
            r = prices[pr]
            if l<r:
                _p = r - l
                if _p > p: p = _p
                pr+=1
            else:
                pl = pr
                pr += 1
        return p
                
