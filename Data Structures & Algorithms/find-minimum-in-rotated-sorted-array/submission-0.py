class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        lowestNumber = nums[0]

        while left <= right:

            mid = left + (right - left) // 2

            if lowestNumber > nums[left]:
                lowestNumber = nums[left]

            if nums[right] < nums[mid]:
                left = mid + 1
            elif nums[left] < nums[mid]:
                right = mid - 1
            else:
                left += 1
        
        return lowestNumber