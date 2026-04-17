class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = set()

        for num in nums:
            hashmap.add(num)

        if len(hashmap) < len(nums):
                return True

        return False
            


