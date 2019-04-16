class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        j = n-1
        tar= m+n-1
        while j>=0:
            if  i>=0 and nums1[i] > nums2[j]:
                nums1[tar]= nums1[i] 
                i=i-1
            else:
                nums1[tar]= nums2[j]
                j=j-1
            tar =tar -1
