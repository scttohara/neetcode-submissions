class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        listForward = [0] * len(nums)
        for index in range(len(nums)):

            if index == 0:
                listForward[index] = nums[index]
            elif index > 0:
                listForward[index] = listForward[index - 1] * nums[index] 


        listBackward = [0] * len(nums)
        for index in range(len(nums) - 1, -1,-1):
            if index == len(nums) - 1:
                listBackward[index] = nums[index]
            elif index < len(nums):
                listBackward[index] = listBackward[index + 1] * nums[index]

        finalList = [0] * len(nums)
        for index in range(len(nums)):

            if index == 0:
                finalList[index] = listBackward[index + 1]
            elif index + 1 < len(nums):
                finalList[index] = listForward[index - 1] * listBackward[index + 1]
            else:
                finalList[index] = listForward[index - 1]

        return finalList