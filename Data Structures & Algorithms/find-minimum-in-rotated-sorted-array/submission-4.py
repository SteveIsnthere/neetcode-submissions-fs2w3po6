class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        md = int((l+r)/2)
        while abs(l-r)>1:
            if nums[md]>nums[r]:
                l = md
            else:
                r = md
            md = int((l+r)/2)
        return min(nums[l],nums[r])