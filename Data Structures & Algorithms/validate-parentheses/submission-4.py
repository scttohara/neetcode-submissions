class Solution:
    def isValid(self, s: str) -> bool:
        # Done using a loop up dict
        stack = []
        lookup_dict = {')':'(', ']':'[', '}':'{'}

        for character in s:

            if character in lookup_dict:

                if stack and stack[-1] == lookup_dict[character]:
                    stack.pop()

                else:
                    return False
            
            else:
                stack.append(character)
        
        if stack != []:
            return False
    
        return True

        # Below done without a lookup dict. O(n) and O(n) space comp.
        """if len(s) < 2:
            return False
        
        stack = []
        for index in range(len(s)):

            if s[index] in '([{':
                stack.append(s[index])

            elif s[index] in ')]}':
            
                if stack == []:
                    return False

                last_add = stack.pop()

                if s[index] == ')' and last_add != '(':
                    return False
                elif s[index] == ']' and last_add != '[':
                    return False
                elif s[index] == '}' and last_add != '{':
                    return False
                else:
                    continue

        if stack != []:
            return False

        return True"""

        """#Brute force. O(n^2) and O(n) space comp.
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()', '')
            s = s.replace('{}', '')
            s = s.replace('[]', '')
        return s == ''"""