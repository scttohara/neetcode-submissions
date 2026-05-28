class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        left_pointer = 0
        right_pointer = len(heights) - 1
        while left_pointer < right_pointer:

            curr_value = (right_pointer - left_pointer) * min(heights[left_pointer], heights[right_pointer])

            if curr_value > max_water:
                max_water = curr_value
            
            if heights[left_pointer] < heights[right_pointer]:
                left_pointer += 1
                continue
            elif heights[left_pointer] > heights[right_pointer]:
                right_pointer -= 1
                continue
            else:
                left_pointer += 1

        return max_water