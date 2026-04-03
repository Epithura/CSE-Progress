class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i=0
        j=0
        L=[]
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<=nums2[j]:
                L.append(nums1[i])
                i=i+1
            else:
                L.append(nums2[j])
                j=j+1
        if i==len(nums1):
            L.extend(nums2[j:])
        else:
            L.extend(nums1[i:])
        if len(L)%2==0:
            return (L[len(L)//2] + L[(len(L)//2)-1])/2
        else:
            return L[len(L)//2]