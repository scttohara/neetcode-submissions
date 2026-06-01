class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        for character in tokens:

            if character == '+':
                stack.append(stack.pop() + stack.pop())

            elif character == '-':
                positionTwo = stack.pop()
                positionOne = stack.pop()
                stack.append(positionOne - positionTwo)

            elif character == '*':
                stack.append(stack.pop() * stack.pop())

            elif character == '/':
                positionTwo = stack.pop()
                positionOne = stack.pop()
                stack.append(int(float(positionOne) / positionTwo))
            else:
                stack.append(int(character))
        
        return stack[0]
        
        
        #First attempt. very slow
        """stack = []
        for character in tokens:

            if character.isnumeric() or character[1:].isnumeric():
                stack.append(character)
            
            else:
                positionTwo = stack.pop()
                positionOne = stack.pop()

                if character == '/':
                    newNumber = int(eval(positionOne + character + positionTwo))
                else:
                    newNumber = eval(positionOne + character + positionTwo)

                stack.append(str(newNumber))
        
        return int(stack[0])"""