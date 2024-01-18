class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1_dupp = set()
        nums2_dupp = set()
        for num in nums1:
            if num not in nums2 and num not in nums1_dupp:
                nums1_dupp.add(num)

        for num2 in nums2:
            if num2 not in nums1_dupp and num2 not in nums1:
                nums2_dupp.add(num2)

        return [nums1_dupp,nums2_dupp]        
