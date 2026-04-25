class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashmap_for_s = {}
        hashmap_for_t = {}

        for chars1 in s:
            if chars1 in hashmap_for_s:
                hashmap_for_s[chars1] += 1
            else:
                hashmap_for_s[chars1] = 1
        
        for chars2 in t:
            if chars2 in hashmap_for_t:
                hashmap_for_t[chars2] += 1
            else:
                hashmap_for_t[chars2] = 1

        if hashmap_for_s == hashmap_for_t:
            return True
        
        return False