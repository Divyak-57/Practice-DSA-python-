class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict = {}
        if(len(s) != len(t)):
            return False
        for i in s:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
        for i in range(len(t)):
            if t[i] not in dict or dict[t[i]]==0:
                return False
            dict[t[i]]-=1
        return True

        
