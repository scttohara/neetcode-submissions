class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        from collections import defaultdict
        dictForReturn = {}

        for strings in strs:

            freq = [0] * 26
            for chars in strings:
                freq[ord(chars) - ord('a')] += 1

            if tuple(freq) in dictForReturn:
                dictForReturn[tuple(freq)] += [strings]
            else:
                dictForReturn[tuple(freq)] = [strings]

        test = dictForReturn.values()
        return list(test)