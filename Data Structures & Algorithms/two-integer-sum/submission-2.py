class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compSeen = {}
        index = 0
        for number in nums:

            compliment = target - number

            if compliment in compSeen:
                return [compSeen[compliment], index]
            else:
                compSeen[number] = index
            
            index += 1