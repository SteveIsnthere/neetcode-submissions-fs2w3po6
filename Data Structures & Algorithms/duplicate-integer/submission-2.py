class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_items = set()
        for n in nums:
            if n in seen_items: return True
            seen_items.add(n)
        return False