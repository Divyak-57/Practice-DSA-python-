class Solution:
    def reverseWords(self, s: str) -> str:
        word = s.split()
        ans = ""
        for i in range(len(word)-1,-1,-1): #O(n^2)
            ans+=word[i]
            ans+=" "
        return ans.strip() # remove extra space from answer in both starting and ending


# another appraoch O(n)
class Solution:

    def reverseWords(self, s: str) -> str:
        words = s.split()
        return " ".join(words[::-1])
        
