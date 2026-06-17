class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dictForS = {}
        for char in s:
            if char in dictForS:
                dictForS[char] += 1
            else:
                dictForS[char] = 1
        
        dictForT = {}
        for char in t:
            if char in dictForT:
                dictForT[char] += 1
            else:
                dictForT[char] = 1

        if dictForS == dictForT:
            return True
        
        return False