class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        groupOfWords = defaultdict(list)
        for string in strs:

            freq = [0] * 26 
            for char in string:

                freq[ord(char) - ord('a')] += 1

            groupOfWords[tuple(freq)].append(string)

        return list(groupOfWords.values())