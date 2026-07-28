class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        for j in range(1,n):
            if(nums[i]<nums[j]): # agar yeh condition nhi fulfil hogi toh sirf j increment hoga i wahi rahega joh tha
                x = nums[i+1] # agar fulfil hogi toh swapping hogi taki duplicate ko piche kar sake 
                nums[i+1] = nums[j]
                nums[j] = x
                i+=1
        return i+1 # kyuki 0 indexing h isliye length +1 hoga
        
