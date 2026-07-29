class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for s in strs:
            chars = sorted(s)
            new_chars = "".join(chars)

            if(new_chars not in dict):
                dict[new_chars]=[]
            dict[new_chars].append(s)
        return list(dict.values())

        
