class Solution:

    def encode(self, strs: List[str]) -> str:
        newString = ""
        for string in strs:
            newString += string + "🚀"

        return newString

    def decode(self, s: str) -> List[str]:

        returnList = []
        index = 0
        tempString = ""
        while index < len(s):

            if s[index] == "🚀":
                returnList.append(tempString)
                tempString = ""
            else:
                tempString += s[index]
 
            index += 1

        return returnList

        