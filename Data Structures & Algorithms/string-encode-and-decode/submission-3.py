class Solution:

    def encode(self, strs: List[str]) -> str:
        return_string = ""
        if strs == [""]:
            return return_string
        
        elif strs == []:
            return return_string + "🎉"

        for position in strs:
            if return_string == "":
                return_string = position + "🎉"

            else:
                return_string += position + "🎉"
            
        return return_string

    def decode(self, s: str) -> list[str]:
        
        list_of_strings = []
        temp_string = ""
        if s == "":
            return [s]
        elif s == "🎉":
            return []
        
        for character in s:

            if character == "🎉":
                list_of_strings.append(temp_string) 
                temp_string = ""
            else:
                temp_string += character
        
        return list_of_strings