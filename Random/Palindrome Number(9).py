class Solution:
    def isPalindrome(self, x: int) -> bool:
        chars = list(str(x)) # phale diya hua number ko string me h then list me
        b = chars.copy() # ek copy bana lenge 
        b.reverse() # reverse kar lenge copy ka
        if(chars==b): # check karenge copy aur orignal same h toh true nhi toh false
            return True
        else:
            return False

        
