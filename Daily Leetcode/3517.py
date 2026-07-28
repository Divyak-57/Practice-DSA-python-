class Solution:
    def smallestPalindrome(self, s: str) -> str:
        length = len(s)
        part = length//2
        chars = list(s)
        chars[:part] = sorted(chars[:part])
        for i in range(part):
            chars[length-1-i]=chars[i]
        return "".join(chars)
        
