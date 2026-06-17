class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        seen = {}
        for number in nums:
            if number in seen:
                return True
            else:
                seen[number] = number
        return False
            


