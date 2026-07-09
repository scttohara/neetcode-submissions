class Solution:
	def hasDuplicate(self, nums: List[int]) -> bool:
		
		if len(nums) <= 0:
			return False

		seen = set()
		for number in nums:

			if number in seen:
				return True
			else:
				seen.add(number)

		return False

        


