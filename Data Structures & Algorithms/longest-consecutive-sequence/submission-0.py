class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # create set from input array (for membership testing)
        set_nums = set(nums)
        current_longest = 0 #keep track of length of longest sequence

        #iterate through input array
        for number in nums: 
            #check if the (current number - 1) is in the set_nums
            if (number - 1) in set_nums: 
                continue #if so, not the start of sequence 
            #check if the (current number - 1) is not in the set_nums
            if (number - 1) not in set_nums:
                #count for length of current sequence 
                count = 1 
                #iterate through current continuos sequence until it ends
                while (number + count) in set_nums:  
                    count += 1 #increase count
                    
                #update current longest seen sequence 
                current_longest = max(count, current_longest)
        
        return current_longest