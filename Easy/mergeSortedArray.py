class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #This solution makes use of the sort method in python.
        #All the zeros in nums1 are replaced with the elements in nums2,
        #then nums1 is sorted to give the final output
        j=0   
        for i in range(m,m+n):
            nums1[i] = nums2[j]
            j+=1
            
            if j==n:
                break
        
        nums1 = nums1.sort()
