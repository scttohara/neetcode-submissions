class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        #how to solve with regex and some of library calls in this comment
        import re

        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s = s.lower()
        s_no_gaps = s.replace(" ", "")
        s_no_gaps_reversed = s_no_gaps[::-1]
        return s_no_gaps == s_no_gaps_reversed"""
        
        # How to solve using two pointers 
        """if len(s) == 1:
            return True"""
        
        pointer_1 = 0
        pointer_2 = (len(s) - 1)
        #test = len(s) / 2
        while pointer_1 < len(s):
            #print(s[pointer_1], s[pointer_2])
            if not s[pointer_1].isalnum():
                pointer_1 += 1
                continue
            if not s[pointer_2].isalnum():
                pointer_2 -= 1
                continue
            if s[pointer_1].lower() != s[pointer_2].lower():
                return False
            
            pointer_1 += 1
            pointer_2 -= 1

        return True