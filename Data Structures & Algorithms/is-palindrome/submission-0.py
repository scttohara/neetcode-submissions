class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re

        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s = s.lower()
        s_no_gaps = s.replace(" ", "")
        s_no_gaps_reversed = s_no_gaps[::-1]
        return s_no_gaps == s_no_gaps_reversed