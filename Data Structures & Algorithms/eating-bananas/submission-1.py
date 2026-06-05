class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #O(n * log m)
        #space: (1)
        left = 1
        right = max(piles)

        #listToReturn = []
        while left <= right:
            
            mid = left + (right - left) // 2

            index = 0 
            counter = 0
            while index < len(piles):
                counter += -(piles[index] // -mid)
                index += 1

            if counter <= h:
                #listToReturn.append(mid)
                right = mid - 1
            else:
                left = mid + 1
 
        return left
        
        # This solution below is O(max(piles) * n) 
        # max(piles) is the largest pile and n is the length of piles
        minNeeded = 1
        counter = 0
        index = 0
        
        while index < len(piles):
            while index < len(piles) and counter <= h:
                currValue = piles[index] # current value variable so the input array is reusable each loop
                counter += -(currValue // -minNeeded) # -(a // -b) does ceiling division without needing to import a lib
                index += 1
            
            if counter > h: #reset if current eating speed isn't fast enough
                
                counter = 0
                minNeeded += 1
                index = 0

            else:
                return minNeeded

        return minNeeded