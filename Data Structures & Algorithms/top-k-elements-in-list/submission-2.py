class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dictForCount = {}
        for number in nums:
            if number in dictForCount:
                dictForCount[number] += 1
            else:
                dictForCount[number] = 1

        keyList = []
        countList = []
        for key, count in zip(dictForCount.keys(), dictForCount.values()):
            keyList.append(key)
            countList.append(count)

        listToReturn = [0] * k
        count = 0
        while count < k:
            indexOfCurrMax = countList.index(max(countList))
            listToReturn[count] = keyList[indexOfCurrMax]
            countList.pop(indexOfCurrMax)
            keyList.pop(indexOfCurrMax)
            count += 1

        return listToReturn
        