class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """#Brute force
        pointer_1 = 0
        pointer_2 = 1

        while pointer_2 < len(numbers):

            if numbers[pointer_1] + numbers[pointer_2] == target:
                return [pointer_1 + 1, pointer_2 + 1]
            if pointer_2 != (len(numbers) - 1):
                pointer_2 += 1
                continue
            if pointer_2 == (len(numbers) - 1):
                pointer_1 += 1
                pointer_2 = pointer_1 + 1

        return []"""

        #using binary search
        for curr_index in range(len(numbers)):
            left_index, right_index = curr_index + 1, len(numbers) - 1
            complement = target - numbers[curr_index]

            while left_index <= right_index:
                curr_mid = (left_index + right_index)//2
                if numbers[curr_mid] == complement:
                    return [curr_index + 1, curr_mid + 1]
                elif numbers[curr_mid] < complement:
                    left_index = curr_mid + 1
                else:
                    right_index = curr_mid - 1

        return []