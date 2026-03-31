class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            
            # Identify which half is sorted
            if nums[l] <= nums[mid]:
                # Left half is sorted
                if nums[l] <= target < nums[mid]:
                    r = mid - 1 # Target is in sorted left half
                else:
                    l = mid + 1 # Target is in right half
            else:
                # Right half is sorted
                if nums[mid] < target <= nums[r]:
                    l = mid + 1 # Target is in sorted right half
                else:
                    r = mid - 1 # Target is in left half
                    
        return -1