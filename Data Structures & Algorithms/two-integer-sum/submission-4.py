class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compSeen = {}

        for index in range(len(nums)):

            complement = target - nums[index]
            if nums[index] in compSeen:
                return [compSeen[nums[index]], index]
            else:
                compSeen[complement] = index
        
        return []