class Solution:
    def search(self, nums: List[int], target: int) -> int:
        leftIndex = 0
        rightIndex = len(nums) - 1
        while leftIndex <= rightIndex:

            mid = leftIndex + (rightIndex - leftIndex) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                rightIndex = mid - 1
            elif nums[mid] < target:
                leftIndex = mid + 1
            
        return -1