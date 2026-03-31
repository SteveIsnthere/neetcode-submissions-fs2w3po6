class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i in range(len(nums)):
            hm[nums[i]] = i

        for i in range(len(nums)):
            n = nums[i]
            diff = target - n
            if diff in hm and hm[diff] != i:
                res = [i, hm[diff]]
                res.sort()
                return res