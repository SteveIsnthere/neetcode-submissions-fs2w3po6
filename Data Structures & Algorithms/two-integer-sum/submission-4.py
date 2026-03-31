class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for k in range(i+1, len(nums)):
                if nums[i] + nums[k] == target: return [i,k]

        return [0,0]