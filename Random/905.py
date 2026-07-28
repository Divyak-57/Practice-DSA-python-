class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i=0
        for j in range(n):
            if nums[j]%2 == 0:
                temp = nums[j]
                nums[j] = nums[i]
                nums[i] = temp
                i+=1
        return nums
        
