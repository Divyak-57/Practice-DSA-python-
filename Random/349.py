class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1)&set(nums2)) # set me covert kar lenge kyuki woh sirf unique element rakhta h aur & intersectin de dega

        
