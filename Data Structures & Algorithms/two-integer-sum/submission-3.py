class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compSeen = {}
        index = 0
        for number in nums:

            complement = target - number

            if complement in compSeen:
                return [compSeen[complement], index]
            else:
                compSeen[number] = index
            
            index += 1