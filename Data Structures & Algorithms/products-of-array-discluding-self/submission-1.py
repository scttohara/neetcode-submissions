class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #creates prefix product array
        current_index = 0
        prefix_product_array = [0] * len(nums)
        while current_index < len(nums):
            if current_index == 0:
                prefix_product_array[current_index] = nums[current_index]
            else:
                prefix_product_array[current_index] = nums[current_index] * prefix_product_array[current_index - 1]

            current_index += 1
        
        #creates suffix product array
        second_current_index = len(nums) - 1
        suffix_product_array = [0] * len(nums)
        while second_current_index > -1:
            if second_current_index == len(nums) - 1:
                suffix_product_array[second_current_index] = nums[second_current_index]
            else:
                suffix_product_array[second_current_index] = nums[second_current_index] * suffix_product_array[second_current_index + 1]

            second_current_index -= 1

        #makes the final array
        last_current_index = 0
        array_to_return = [0] * len(nums)
        while last_current_index < len(nums):

            if last_current_index == 0:
                array_to_return[last_current_index] = 1 * suffix_product_array[last_current_index + 1]
            elif last_current_index + 1 == len(nums):
                array_to_return[last_current_index] = prefix_product_array[last_current_index - 1] * 1
            else:
                array_to_return[last_current_index] = prefix_product_array[last_current_index - 1] * suffix_product_array[last_current_index + 1]

            last_current_index += 1

        return array_to_return