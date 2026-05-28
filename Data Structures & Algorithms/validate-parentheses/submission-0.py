class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
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

        return True