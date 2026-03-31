class Solution:
    def maxArea(self, heights: List[int]) -> int:
        pl = 0
        pr = len(heights) - 1
        m_a = 0
        while pl < pr:
            w = pr - pl
            l = heights[pl]
            r = heights[pr]
            a = min(l,r) * w
            if a > m_a: m_a = a
            if max(l,r) == l:
                pr -= 1
            else:
                pl += 1

        return m_a