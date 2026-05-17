from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]
        
        list_to_return = defaultdict(list)
        for current_string in strs:

            current_string_count = [0] * 26
            for char in current_string:
                current_string_count[ord(char) - ord('a')] += 1

            list_to_return[tuple(current_string_count)].append(current_string)
            
        return list(list_to_return.values())