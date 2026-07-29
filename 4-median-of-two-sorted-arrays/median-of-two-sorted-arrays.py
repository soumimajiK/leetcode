class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        tog=nums1+nums2
        tog.sort()
        if len(tog)%2==0:
            one=len(tog)//2 - 1
            two=one+1
            med=(tog[one]+tog[two])/2
        else:
            mid=len(tog)//2
            med=tog[mid]
        return med