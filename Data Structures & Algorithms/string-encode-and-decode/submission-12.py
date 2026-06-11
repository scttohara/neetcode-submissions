class Solution:

    def encode(self, strs: List[str]) -> str:

        encodedString = ""
        for strings in strs:

            encodedString += strings + "🚀"
        
        return encodedString

    def decode(self, s: str) -> list[str]:
        
        decodedStrings = []
        tempString = ""
        index = 0
        while index < len(s):

            if s[index] == "🚀":
                decodedStrings.append(tempString)
                tempString = ""
                
            else:
                tempString += s[index]
                
            index += 1

        return decodedStrings