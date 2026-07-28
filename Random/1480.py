class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums) 
        ans = [nums[0]] # ans list bana lenge aur 0 index par nums[0] store kara denge
        for i in range(1,n): # aab 1 se n-1 tak check karenge
            ans.append(ans[i-1]+nums[i]) # ans me add karenge
        return ans    
