class Solution:
    def isAlphaNum(self, s: str)->bool:
        x = ord(s)
        if(97<=x<=122 or 48<=x<=57):
            return True
        return False

    def isPalindrome(self, s: str) -> bool:
        l , r = 0 , len(s)-1
        s = s.lower()
        while(l<=r):
            if not self.isAlphaNum(s[l]):
                l+=1
                continue
            if not self.isAlphaNum(s[r]):
                r-=1
                continue
            if(s[l] != s[r]):
                return False
            l+=1
            r-=1
        return True
        
