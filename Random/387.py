class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {} # frequency array bana lenge
        for i in s:
            if i not in freq:
                freq[i] = 1 # agar first time aaya
            else:
                freq[i]+=1 # agar phale v tha
        for i in range(len(s)):
            if freq[s[i]] == 1:
                return i
        return -1

        
        
