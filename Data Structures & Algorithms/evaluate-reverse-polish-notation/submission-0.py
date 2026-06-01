class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
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
        
        return int(stack[0])