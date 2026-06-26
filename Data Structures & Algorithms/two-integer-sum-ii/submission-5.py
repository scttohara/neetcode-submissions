class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        """while left < right:

            mid = left + (right - left) // 2

            if numbers[mid] < target:
                left = mid - 1
            elif numbers[mid] > target:
                right = mid - 1"""
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
        return []