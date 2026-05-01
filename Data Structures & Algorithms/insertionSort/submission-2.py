# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        
        if pairs == []:
            return []
        list_to_return = [pairs[:]]
        counter = 1
        #list_to_return.append(pairs[:])
        while counter < len(pairs):

            counter_2 = counter

            while counter_2 > 0 and pairs[counter_2 - 1].key > pairs[counter_2].key:

                pairs[counter_2], pairs[counter_2 - 1] = pairs[counter_2 - 1], pairs[counter_2]

                counter_2 = counter_2 - 1
                #list_to_return.append(pairs)
            
            counter = counter + 1
            list_to_return.append(pairs[:])
        
        return list_to_return