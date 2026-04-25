class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #create a dict called "hashmap"
        hashmap = dict()

        #using a for loop interate through "nums" 
        for integer in range(len(nums)):
            #complement is equal to "target" minus current number in a given indices of "nums"
            complement = target - nums[integer] 
            #if the complement is present in "hashmap" we have a solution and can return both indices of the current numbers
            if complement in hashmap:
                return [hashmap[complement], integer]
            #else we store the current number from "nums" and its indice as a key:value pair
            hashmap[nums[integer]] = integer