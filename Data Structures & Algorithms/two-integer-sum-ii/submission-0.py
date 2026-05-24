class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
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
